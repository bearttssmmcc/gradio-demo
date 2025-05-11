# Gradio Demo (RGB Color Generator)

![](./doc/screenshot.jpg)

## Run locally

Build

```bash
docker build -t color-generator .
```

Start container

```bash
docker run d -p 7860:7860 --name my-color-app color-generator
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

## Cloud Build

Copy the `build/main-cloudbuild.yaml.tmpl` to `build/main-cloudbuild.yaml`, and replace the placeholder:
- `$PROJECT_ID`
- `$LOCATION`
- `$AR_REPO_NAME`
- `$CLUSTER`

For example, you can do the task by bash commands:

```bash
export PROJECT_ID=$(gcloud config get-value project)
export LOCATION=us-central1
export CLUSTER=gke-progression-cluster
export AR_REPO_NAME=ntu-lab-repo
```

```bash
for template in $(find . -name '*.tmpl'); do envsubst '${PROJECT_ID} ${LOCATION} ${CLUSTER} ${AR_REPO_NAME}' < ${template} > ${template%.*}; done
```

## Kubernetes YAML

Assume push the iamge to Google Artifact Registry(us-central1).

Copy the `k8s/deployment.yaml.tmpl` to `k8s/deployment.yaml`, and replace the placeholder:
- `$PROJECT_ID`
- `$AR_REPO_NAME`

For example, you can do the task by bash commands:
(you can skip it if you have executed it in Cloud Build section)

```bash
export PROJECT_ID=$(gcloud config get-value project)
export LOCATION=us-central1
export CLUSTER=gke-progression-cluster
export AR_REPO_NAME=ntu-lab-repo
```

```bash
for template in $(find . -name '*.tmpl'); do envsubst '${PROJECT_ID} ${LOCATION} ${CLUSTER} ${AR_REPO_NAME}' < ${template} > ${template%.*}; done
```

Apply to GKE

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

Wait the external IP ready

```bash
kubectl get service color-generator-external
```

Access the external IP in browser.
