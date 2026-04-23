# AI 주차 관리 시스템

YOLOv8 ONNX 기반 브라우저 네이티브 주차 탐지 시스템

## 특징

- 서버리스: GitHub Pages에 배포 가능
- 온디바이스 AI: ONNX Runtime Web으로 브라우저에서 직접 추론
- 멀티 입력: 웹캠, 이미지, 비디오 지원
- 소스별 설정: 각 입력 소스마다 독립적인 주차 구역 좌표 저장
- LocalStorage: 브라우저 로컬 스토리지에 설정 영구 저장

## 시작하기

### 1. YOLOv8 모델 준비

YOLOv8n 모델을 ONNX 형식으로 변환하여 `/models/` 폴더에 배치하세요:

```python
from ultralytics import YOLO
model = YOLO('yolov8n.pt')
model.export(format='onnx', opset=12)
```

생성된 `yolov8n.onnx` 파일을 `Source/models/` 폴더에 복사하세요.

### 2. 로컬 실행

간단한 HTTP 서버로 실행:

```bash
cd Source
python -m http.server 8000
```

http://localhost:8000 에 접속하세요.

### 3. GitHub Pages 배포

1. 이 레포지토리를 GitHub에 푸시
2. Settings > Pages에서 Source 폴더를 루트로 설정
3. `yolov8n.onnx` 모델 파일이 포함되어 있는지 확인

## 사용법

1. **입력 소스 선택**: 상단 탭에서 웹캠, 이미지, 비디오 중 선택
2. **주차 구역 설정**:
   - 설정 모드에서 캔버스 클릭으로 점 추가
   - 더블클릭으로 다각형 완성
   - 설정 저장 버튼으로 좌표 저장
3. **감시 모드**: AI가 실시간으로 주차 상태 감지

## 브라우저 호환성

- Chrome 90+
- Edge 90+
- Firefox 88+
- Safari 15+

WebAssembly, Canvas API, LocalStorage를 지원하는 브라우저가 필요합니다.
