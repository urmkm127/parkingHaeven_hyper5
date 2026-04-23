# YOLOv8 모델 파일

이 폴더에는 YOLOv8 ONNX 모델 파일이 필요합니다.

## 모델 변환 방법

### Python 환경에서:

```bash
pip install ultralytics onnx onnxruntime
```

```python
from ultralytics import YOLO

# YOLOv8n 모델 로드
model = YOLO('yolov8n.pt')

# ONNX로 내보내기 (opset 12 권장)
model.export(format='onnx', opset=12, simplify=True)
```

생성된 `yolov8n.onnx` 파일을 이 폴더에 배치하세요.

## 모델 정보

- **모델**: YOLOv8 Nano (가장 가볍고 빠름)
- **입력 크기**: 640x640
- **클래스**: person, bicycle, car, motorcycle, 등 (COCO 80클래스)
- **용도**: 주차된 차량 탐지

## 대체 모델

더 정확한 탐지를 원한다면 YOLOv8s 또는 YOLOv8m을 사용할 수 있습니다:

```python
# 더 정확하지만 느린 모델
model = YOLO('yolov8s.pt')  # Small
model = YOLO('yolov8m.pt')  # Medium
```

주의: 더 큰 모델은 브라우저 로딩 시간이 길어집니다.
