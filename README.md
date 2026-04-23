# AI 주차 관리 시스템

YOLOv8 ONNX 기반 브라우저 네이티브 주차 탐지 시스템

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 프로젝트 개요

서버 없이 브라우저에서 직접 실행되는 AI 주차 관리 시스템입니다. YOLOv8 ONNX 모델을 사용하여 웹캠, 이미지, 비디오에서 실시간으로 주차된 차량을 탐지하고 주차 구역별 점유 상태를 관리합니다.

## 주요 특징

- **서버리스 배포**: GitHub Pages에 바로 배포 가능
- **온디바이스 AI**: ONNX Runtime Web으로 브라우저에서 직접 추론
- **멀티 입력 지원**: 웹캠, 정지 이미지, 비디오 파일
- **소스별 설정**: 각 입력 소스마다 독립적인 주차 구역 좌표 저장
- **LocalStorage 영구 저장**: 브라우저 로컬 스토리지에 설정 저장
- **실시간 모니터링**: 주차 구역별 점유 상태 시각화 (적색/녹색)
- **반응형 UI**: Tailwind CSS 기반 현대적 대시보드

## 프로젝트 구조

```
ParkingHaeven/
├── Source/              # 배포용 웹 앱 (GitHub Pages 루트)
│   ├── index.html      # 메인 페이지
│   ├── js/             # JavaScript 모듈
│   ├── models/         # YOLOv8 ONNX 모델
│   └── samples/        # 테스트용 샘플 파일
├── Doc/                # 프로젝트 문서
│   ├── PRD.md          # 제품 요구사항
│   ├── TRD.md          # 기술 설계서
│   ├── UserFlow.md     # 사용자 흐름
│   └── Instruction.md  # 개발 가이드
└── README.md           # 이 파일
```

## 시작하기

### 1. 모델 준비

YOLOv8n 모델을 ONNX 형식으로 변환하여 `Source/models/` 폴더에 배치하세요.

**Python이 있는 환경에서:**

```bash
pip install ultralytics onnx onnxruntime
```

```python
from ultralytics import YOLO

# YOLOv8n 모델 로드
model = YOLO('yolov8n.pt')

# ONNX로 변환 (opset 12 권장)
model.export(format='onnx', opset=12, simplify=True)
```

생성된 `yolov8n.onnx` 파일을 `Source/models/` 폴더에 복사하세요.

### 2. 로컬 실행

간단한 HTTP 서버로 실행:

```bash
cd Source
python3 -m http.server 8000
```

브라우저에서 http://localhost:8000 접속

### 3. 샘플 파일 추가

테스트용 이미지/비디오를 샘플 폴더에 넣으세요:

```
Source/samples/images/   # 주차장 이미지
Source/samples/videos/   # 주차장 비디오
```

### 4. GitHub Pages 배포

1. 이 레포지토리를 GitHub에 푸시
2. **Settings** > **Pages** 진입
3. **Source**: `Deploy from a branch`
4. **Branch**: `main` / `Source` 폴더
5. **Save`

### 5. 좌표 공유 (선택)

다른 사용자와 주차 구역 좌표를 공유할 수 있습니다:

1. 주차 구역 설정 후 **📤 현재 파일 좌표 내보내기**
2. 다운로드된 JSON 파일을 `samples/coordinates/` 폴더에 저장
3. 깃에 커밋하여 공유

다른 사용자는 **📥 좌표 가져오기**로 불러올 수 있습니다.

## 사용법

### 설정 모드

#### 주차 구역 개념 이해하기

**중요**: 1개 다각형 = 1대 주차면

- 각 다각형은 **한 대의 차가 주차할 수 있는 개별 공간**입니다
- 주차장에 10대를 주차하려면 **10개의 다각형**을 그려야 합니다
- 각 다각형은 독립적으로 "점유/잔여" 상태를 표시합니다

```
예시: 6면 주차장 설정
┌─────────────────────────────┐
│ [1] [2] [3]                │  ← 각 숫자 = 1개 다각형
│                             │     (총 6개 그려야 함)
│ [4] [5] [6]                │
└─────────────────────────────┘
```

#### 설정 순서

1. **입력 소스 선택**: 상단 탭에서 웹캠, 이미지, 비디오 중 선택
2. **샘플 파일 사용**: "샘플 파일" 목록에서 파일 클릭
3. **첫 번째 주차면 그리기**:
   - "+ 주차 구역 추가" 버튼 클릭
   - 캔버스를 클릭하여 점 추가 (최소 3개)
   - Enter 또는 더블클릭으로 다각형 완성
   - 점을 드래그하여 위치 수정
4. **두 번째 주차면 그리기**: 다시 "+ 주차 구역 추가" → 반복
5. **저장**: Ctrl+S 또는 "설정 저장" 버튼

### 감시 모드

1. **감시 모드 전환**: 우측 상단 "감시 모드" 버튼 클릭
2. **AI 탐지 시작**: YOLOv8이 실시간으로 차량 탐지
3. **상태 확인**:
   - 🔴 적색: 점유 중
   - 🟢 녹색: 잔여
   - 대시보드에 잔여면수 표시

### 키보드 단축키

| 단축키 | 기능 |
|--------|------|
| `Enter` | 주차 구역 완료 |
| `Esc` | 구역 추가 취소 |
| `Del` | 선택 구역 삭제 |
| `Ctrl+S` | 설정 저장 |

### 소스별 좌표 관리

각 파일마다 독립적인 주차 구역 좌표가 저장됩니다:

- **웹캠**: `LIVE_WEBCAM`으로 저장
- **파일**: `파일명_파일크기`로 자동 저장

소스를 바꿔도 각 파일에 설정한 좌표가 자동으로 로드됩니다.

## 기술 스택

- **AI 모델**: YOLOv8 Nano (ONNX)
- **추론 엔진**: ONNX Runtime Web
- **프레임워크**: Vanilla JavaScript (ES6 Modules)
- **스타일링**: Tailwind CSS
- **데이터 저장**: LocalStorage

## 브라우저 호환성

- Chrome 90+
- Edge 90+
- Firefox 88+
- Safari 15+

**요구사항**: WebAssembly, Canvas API, LocalStorage 지원

## 아키텍처

### 핵심 모듈

```javascript
js/
├── app.js            # 메인 컨트롤러
├── MediaHandler.js   # 웹캠/이미지/비디오 통합 처리
├── StorageManager.js # LocalStorage 소스별 좌표 관리
├── OverlayRenderer.js# Canvas 오버레이 렌더링
└── YOLODetector.js   # YOLOv8 ONNX 추론 엔진
```

### 데이터 흐름

```
입력 소스 → MediaHandler → Main Canvas
                              ↓
                        YOLODetector
                              ↓
                        OverlayRenderer
                              ↓
                          사용자 UI
```

## 문서

자세한 문서는 `Doc/` 폴더를 참조하세요:

- [PRD.md](Doc/PRD.md) - 제품 요구사항
- [TRD.md](Doc/TRD.md) - 기술 설계서
- [UserFlow.md](Doc/UserFlow.md) - 사용자 흐름

## 라이선스

MIT License

## 기여

이 프로젝트에 관심을 가져주셔서 감사합니다!

## 문의

이슈를 등록해주시면 빠르게 답변드리겠습니다.
