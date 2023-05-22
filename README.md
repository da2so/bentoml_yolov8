# bentoml_yolov8


# Setup

```
pip3 install -r requirments.txt
```

# Use 

```
python3 bento_packer.py
bentoml build
DOCKER_BUILDKIT=0 bentoml containerize yolov8s_svc:latest
docker run -it --gpus "device=0" --ipc=host --name yolov8s_model -p 3000:3000 yolov8s_svc:latest
```


