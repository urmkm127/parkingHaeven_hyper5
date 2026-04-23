# TRD: 상세 아키텍처 및 데이터 스키마 설계

## 1. 입력 처리 및 렌더링 파이프라인
- **Source Selection:** 소스 타입(Webcam/Image/Video)에 관계없이 내부적으로는 하나의 `MainCanvas`로 픽셀 데이터를 전달.
- **Video Handling:** 영상 소스는 자동 반복 재생(Loop) 및 프레임 추출 로직 포함.

## 2. 소스별 데이터 매핑 (Scoped Storage Strategy)
- **SourceID 생성:** - 웹캠: `"LIVE_WEBCAM"`
  - 파일: `File.name` + `File.size` (중복 방지용 고유 식별자)
- **데이터 스키마 (LocalStorage):**
  ```json
  {
    "PARKING_SYSTEM_CONFIG": {
      "SOURCE_ID_1": [ {"id": 1, "points": [{"x": 10, "y": 20}, ...]}, ... ],
      "SOURCE_ID_2": [ ... ]
    }
  }