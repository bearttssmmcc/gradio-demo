import gradio as gr

# --- 核心顏色轉換邏輯 ---
def rgb_to_hex(r, g, b):
    """將 RGB 整數值轉換為十六進位顏色碼"""
    r, g, b = int(r), int(g), int(b) # 確保是整數
    return f"#{r:02x}{g:02x}{b:02x}"

def create_color_block_html(hex_color, text=""):
    """創建一個 HTML 色塊來顯示顏色"""
    # 簡單計算亮度決定文字顏色
    try:
        r_val = int(hex_color[1:3], 16)
        g_val = int(hex_color[3:5], 16)
        b_val = int(hex_color[5:7], 16)
        brightness = (r_val * 0.299 + g_val * 0.587 + b_val * 0.114)
        text_color = "#000" if brightness > 128 else "#FFF"
    except (ValueError, IndexError): # 處理無效的 hex_color
        text_color = "#000"
        hex_color = "#FFFFFF" # 預設白色背景以防錯誤

    return f"""
    <div style='
        width: 150px;
        height: 150px;
        background-color: {hex_color};
        border: 2px solid #666;
        border-radius: 10px; /* 圓角 */
        margin: 20px auto; /* 上下間距並水平居中 */
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        font-size: 1.1em;
        color: {text_color};
        text-align: center;
        line-height: 1.2; /* 調整行高以防文字重疊 */
    '>
        {text}
    </div>
    """

# --- Gradio 介面 ---
def create_rgb_color_generator_ui():
    def update_color_display(r, g, b):
        """根據 RGB 值更新顏色預覽和十六進位碼"""
        current_hex = rgb_to_hex(r, g, b)
        display_text = f"R: {int(r)}\nG: {int(g)}\nB: {int(b)}\n<br>{current_hex.upper()}"
        html_block = create_color_block_html(current_hex, text=display_text)
        return html_block, current_hex.upper()

    with gr.Blocks(theme=gr.themes.Glass(), title="RGB 顏色產生器") as demo:
        gr.Markdown(
            """
            # 🌈 RGB 顏色產生器
            拖動下方的滑桿來調整紅 (R)、綠 (G)、藍 (B) 的值，即時查看產生的顏色及其十六進位碼。
            """
        )

        with gr.Row():
            with gr.Column(scale=2): # 滑桿佔用較大空間
                r_slider = gr.Slider(minimum=0, maximum=255, value=128, step=1, label="紅色 (R)")
                g_slider = gr.Slider(minimum=0, maximum=255, value=128, step=1, label="綠色 (G)")
                b_slider = gr.Slider(minimum=0, maximum=255, value=128, step=1, label="藍色 (B)")
            
            with gr.Column(scale=1): # 顏色預覽和色碼佔用較小空間
                color_preview_html = gr.HTML(label="顏色預覽")
                hex_code_output = gr.Textbox(label="十六進位色碼 (Hex)", interactive=False, show_copy_button=True)

        # 收集輸入滑桿
        inputs = [r_slider, g_slider, b_slider]
        # 收集輸出元件
        outputs = [color_preview_html, hex_code_output]

        # 當任何滑桿的值改變時，觸發 update_color_display 函數
        for slider in inputs:
            slider.change(fn=update_color_display, inputs=inputs, outputs=outputs)
        
        # 初始載入時也執行一次，以顯示預設顏色
        demo.load(fn=update_color_display, inputs=inputs, outputs=outputs)

    return demo

if __name__ == "__main__":
    color_generator_app = create_rgb_color_generator_ui()
    color_generator_app.launch()

