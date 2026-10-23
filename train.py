import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolo11.yaml') 
    model.train(data='data.yaml',
                task='detect',
                imgsz=640,
                epochs=300,
                batch=16,
                workers=8,
                device='0',
                optimizer='SGD', 
                project='runs/train',
                name='base',
                )

