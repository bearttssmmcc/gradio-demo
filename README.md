# Gradio Demo (RGB Color Generator)

![](./doc/sceenshot.jpg)

## Run locally

Build

```bash
docker build -t rgb-color-generator .
```

Start container

```bash
docker run d -p 7860:7860 --name my-color-app rgb-color-generator
```

Access

http://localhost:7860

Stop container

```bash
docker stop my-color-app
```

Remove container

```bash
docker rm my-color-app
```
