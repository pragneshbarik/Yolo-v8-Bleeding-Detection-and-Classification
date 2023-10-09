from ultralytics import YOLO



model = YOLO('yolov8x.pt')
model.to('cuda')

results = model.train(
    data="yolo.yaml",
    imgsz=224,
    epochs=500,
    batch=8,
    name='train_valid_4',
    patience=0,
)