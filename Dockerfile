# 使用官方 Python 映像作為基礎映像
# 選擇一個適合你專案的 Python 版本，slim 版本較小
FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 複製依賴性檔案到工作目錄
# 這樣做可以利用 Docker 的層快取機制，如果 requirements.txt 沒有改變，則不需要重新安裝依賴
COPY requirements.txt .

# 安裝依賴性套件
# --no-cache-dir: 不儲存 pip 快取，以減少映像大小
# --trusted-host pypi.python.org: 在某些網路環境下可能需要，用以信任 PyPI
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# 複製應用程式的其餘程式碼到工作目錄
COPY . .

# Gradio 應用程式預設在 7860 連接埠上執行
EXPOSE 7860

# 設定 Gradio 伺服器監聽所有網路介面
# 這樣 Docker 容器外部才能訪問
# Gradio 會自動讀取這個環境變數
ENV GRADIO_SERVER_NAME="0.0.0.0"

# 容器啟動時執行的命令
# 將 "color_generator.py" 替換為你的 Python 腳本檔名
CMD ["python", "color_generator.py"]

