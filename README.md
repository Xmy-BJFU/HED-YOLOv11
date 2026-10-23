# A lightweight edge-based wild boar detection framework for wildlife monitoring and decision support in agroecosystems

Wild boars entering farmland gnaw and trample crops such as maize and rice, reducing yields and intensifying human–wildlife conflict. They are often active in mountainous areas and agroforestry ecotones, where cluttered backgrounds and occlusion by vegetation or other animals are common, while field monitoring devices have limited computing power. Reliable wild boar detection therefore needs to balance accuracy and a lightweight design so that it can run on edge devices and support wildlife monitoring and management decisions in agricultural areas.

This repository implements HED-YOLOv11 for that setting. Built on [Ultralytics YOLO11](https://github.com/ultralytics/ultralytics), the model makes three architectural changes: an HGNetv2 backbone for multi-scale feature extraction, a C2EPSA module to strengthen target features and suppress background interference, and DySample in the neck to improve feature reconstruction under occlusion. The model configuration is `ultralytics/cfg/models/11/yolo11-HGNetV2-X_EMA_Dysample.yaml`.

Training starts from `train.py`. Prepare your own dataset configuration in `data.yaml` before use. This repository is licensed under AGPL-3.0.
