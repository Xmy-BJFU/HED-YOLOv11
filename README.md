# HED-YOLOv11

基于 [Ultralytics YOLO11](https://github.com/ultralytics/ultralytics) 的目标检测改进。HED 对应三处结构改动：

- **H**GNetV2：骨干网络使用 PPHGNetV2（`HGStem` / `HGBlock`）
- **E**MA：在 C2PSA 中加入 EMA 注意力（`C2PSA_EMA`）
- **D**ySample：检测头上采样使用动态上采样（`Dy_Sample`）

改进模型配置：`ultralytics/cfg/models/11/yolo11-HGNetV2-X_EMA_Dysample.yaml`

`train.py` 是训练入口，默认加载基础配置 `yolo11.yaml`。若要训练 HED 结构，将模型路径改为上面的 yaml 即可。数据集配置写在 `data.yaml` 中（需自行准备）。

本仓库遵循 AGPL-3.0 许可证，上游项目为 Ultralytics。
