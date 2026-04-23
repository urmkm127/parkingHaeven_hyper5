# Asset & Implementation Guide

## 1. 필수 라이브러리 (CDN)
- ONNX Runtime Web: `https://cdn.jsdelivr.net/npm/onnxruntime-web/dist/ort.min.js`
- Tailwind CSS: `https://cdn.tailwindcss.com`

## 2. AI 모델 경로
- `/models/yolov8n.onnx` (미리 변환하여 배치 필요)

## 3. 개발 참고 로직 (Core Snippet)
```javascript
// 소스별 데이터 로드 핵심 예시
const currentSourceId = getSourceId(activeFile); 
const savedRegions = JSON.parse(localStorage.getItem('PARKING_SYSTEM_CONFIG'))[currentSourceId] || [];
renderRegions(savedRegions);