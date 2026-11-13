# Computer Vision Term Project

컴퓨터 비전 텀 프로젝트를 위한 Python · PyTorch · OpenCV · Jupyter 시작 환경입니다.
프로젝트 주제와 데이터셋은 아직 정하지 않았습니다.

## 로컬 설치

Python 3.11 또는 3.12를 권장합니다. 아래 명령은 저장소 루트에서 실행합니다.

```bash
git clone https://github.com/yeopsang02/computer_vision_prj.git
cd computer_vision_prj
python -m venv .venv
```

가상환경 활성화:

- macOS / Linux: `source .venv/bin/activate`
- Windows PowerShell: `.venv\Scripts\Activate.ps1`

CPU로 시작하는 Windows / Linux 환경:

```bash
python -m pip install --upgrade pip
python -m pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
python -m pip install -r requirements.txt
python scripts/check_env.py
python -m jupyterlab
```

macOS는 PyTorch 설치 명령을 `python -m pip install torch torchvision`으로 바꿉니다.
NVIDIA GPU를 사용할 경우 [PyTorch 공식 설치 도구](https://pytorch.org/get-started/locally/)에서 운영체제와 지원 CUDA 버전에 맞는 명령으로 torch와 torchvision을 함께 설치하세요. 이 저장소가 CUDA나 GPU 드라이버를 설치하지는 않습니다.

`check_env.py`는 라이브러리 버전, CUDA / MPS / CPU 선택 결과를 출력하고 이미지 처리와 순전파·역전파를 확인합니다. GPU가 없어도 CPU에서 실행됩니다.

## Google Colab

새 Colab 노트북에서 필요하면 **런타임 → 런타임 유형 변경 → GPU**를 선택합니다.
다음 셀을 실행하세요. 매번 새 런타임에서 시작하는 기준입니다.

```python
!git clone https://github.com/yeopsang02/computer_vision_prj.git
%cd /content/computer_vision_prj
%pip install -r requirements.txt
!python scripts/check_env.py
```

Colab에 기본 설치된 torch / torchvision을 먼저 사용합니다. 확인 스크립트가 실패하면 버전 호환성을 확인하세요. 런타임을 종료하면 로컬 파일이 사라질 수 있으므로 데이터와 학습 결과는 Drive 등에 따로 보관하세요.

## 폴더

| 경로 | 용도 |
| --- | --- |
| `src/` | 전처리, 학습, 평가 코드 |
| `notebooks/` | 탐색 및 실험 노트북 |
| `data/` | 데이터 (Git 제외) |
| `checkpoints/` | 학습 가중치 (Git 제외) |
| `outputs/` | 평가 결과 및 시각화 (Git 제외) |
| `scripts/check_env.py` | 실행 환경 검증 |

## 협업과 실험 기록

작업별 브랜치에서 개발하고 Pull Request로 검토합니다. 팀원 초대는 저장소 Settings → Collaborators에서 진행합니다.
실험마다 데이터 분할, seed, 모델, 하이퍼파라미터, 평가 지표를 기록하세요.
기본 의존성은 호환 버전 범위로 관리합니다. 실제 학습 환경이 정해지면 OS·GPU·Python 버전과 함께 `python -m pip freeze` 결과를 보관해 재현성을 확보하세요.

## 다음에 결정할 내용

- 과제 요구사항과 주제: 분류 / 탐지 / 분할 등
- 데이터셋, 라이선스, train / validation / test 분할
- 실행 환경과 GPU 사용 여부
- 기준 모델, 평가 지표, 제출 일정
