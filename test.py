import os
import csv
import torch
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
from PIL import Image
from ultralytics import YOLO


TEST_DATASET = ""
YOLO_WEIGHTS = "/home/mlip/Desktop/bleedgen/yolo_v8_runs/runs/detect/train_valid_4/weights/best.pt"

transform = transforms.Compose([
    transforms.ToTensor(),           
])

class CustomDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.images = os.listdir(root_dir)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        img_name = os.path.join(self.root_dir, self.images[idx])
        image = Image.open(img_name)
        if self.transform:
            image = self.transform(image)
        return img_name, image

test_dataset = CustomDataset(TEST_DATASET, transform=transform)
test_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)

device = "cuda" if torch.cuda.is_available() else "cpu"
yolo_model = YOLO(YOLO_WEIGHTS)

classes = ['bleeding', 'non_bleeding']
with open('predictions.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Image Name', 'Predicted Label(YOLOv8)', 'YOLO CONFIDENCE', "BOUNDING BOXES (xywhn)"])  # Write header

    for image_name, image in test_loader:
        image = image.to(device)
        yolo_predicted_label = "non_bleeding"
        with torch.no_grad():
            results = yolo_model.predict(image / 2.64)
            yolo_row = []
            for result in results :
                conf = result.boxes.conf.tolist()
                if (len(conf) > 0) :
                    yolo_predicted_label = 'bleeding'
                    yolo_row.append(result.boxes.conf.tolist())
                    yolo_row.append(result.boxes.xywhn.tolist())

        writer.writerow([image_name[0].split('/')[-1], yolo_predicted_label] + yolo_row)

print("CSV file with predictions saved as 'predictions.csv'.")