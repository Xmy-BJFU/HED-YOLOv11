# A lightweight edge-based wild boar detection framework for wildlife monitoring and decision support in agroecosystems

本仓库是上述论文的代码补充材料，用于农田和农林交错带中的野猪（*Sus scrofa*）检测。

检测模型为 HED-YOLOv11，在 [Ultralytics YOLO11](https://github.com/ultralytics/ultralytics) 上做了三处改动：HGNetv2 骨干、C2EPSA 注意力，以及颈部的 DySample 上采样，以便在边缘设备上完成轻量化检测。模型配置见 `ultralytics/cfg/models/11/yolo11-HGNetV2-X_EMA_Dysample.yaml`。

训练入口为 `train.py`。使用前请自行准备数据集配置 `data.yaml`。本仓库遵循 AGPL-3.0 许可证。
