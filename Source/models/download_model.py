#!/usr/bin/env python3
"""
YOLOv8n 모델 다운로드 및 ONNX 변환 스크립트
"""
import os
import sys

def main():
    print("=" * 50)
    print("YOLOv8n 모델 다운로드 및 ONNX 변환")
    print("=" * 50)

    # 현재 디렉토리 확인
    current_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_dir)

    # 필수 라이브러리 확인
    try:
        import ultralytics
        print(f"✓ ultralytics 설치됨 (버전: {ultralytics.__version__})")
    except ImportError:
        print("✗ ultralytics가 설치되지 않았습니다.")
        print("설치 명령: pip install ultralytics onnx onnxruntime")
        sys.exit(1)

    try:
        import onnx
        print(f"✓ onnx 설치됨 (버전: {onnx.__version__})")
    except ImportError:
        print("! onnx가 설치되지 않았습니다. ONNX 변환만 진행합니다.")

    # YOLOv8n 모델 로드 및 변환
    print("\n[1/3] YOLOv8n 모델 로드 중...")
    try:
        from ultralytics import YOLO
        model = YOLO('yolov8n.pt')
        print("✓ YOLOv8n 모델 로드 완료")
    except Exception as e:
        print(f"✗ 모델 로드 실패: {e}")
        sys.exit(1)

    # ONNX로 변환
    print("\n[2/3] ONNX 형식으로 변환 중...")
    try:
        model.export(
            format='onnx',
            opset=12,
            simplify=True,
            dynamic=False,
            imgsz=640
        )
        print("✓ ONNX 변환 완료")
    except Exception as e:
        print(f"✗ ONNX 변환 실패: {e}")
        sys.exit(1)

    # 파일 확인
    print("\n[3/3] 파일 확인...")
    onnx_file = os.path.join(current_dir, 'yolov8n.onnx')

    if os.path.exists(onnx_file):
        size_mb = os.path.getsize(onnx_file) / (1024 * 1024)
        print(f"✓ yolov8n.onnx 생성 완료 ({size_mb:.2f} MB)")
        print(f"  위치: {onnx_file}")
    else:
        print("✗ ONNX 파일을 찾을 수 없습니다")
        sys.exit(1)

    # 불필요한 파일 정리
    pt_file = os.path.join(current_dir, 'yolov8n.pt')
    if os.path.exists(pt_file):
        os.remove(pt_file)
        print("✓ 임시 파일 yolov8n.pt 삭제 완료")

    print("\n" + "=" * 50)
    print("모든 작업이 완료되었습니다!")
    print("=" * 50)

if __name__ == "__main__":
    main()
