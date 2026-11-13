"""Verify imports, an OpenCV operation, and a PyTorch forward/backward pass."""
import platform
import cv2
import numpy as np
import torch
import torchvision
import PIL
import matplotlib
import pandas
import sklearn


def main():
    print(f"Python: {platform.python_version()}")
    for module in (np, cv2, torch, torchvision, PIL, matplotlib, pandas, sklearn):
        print(f"{module.__name__}: {module.__version__}")
    device = torch.device("cuda" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
    print(f"Device: {device}")
    if device.type == "cuda":
        print(f"GPU: {torch.cuda.get_device_name(0)}")
    gray = cv2.cvtColor(np.zeros((32, 32, 3), dtype=np.uint8), cv2.COLOR_BGR2GRAY)
    assert gray.shape == (32, 32)
    model = torch.nn.Conv2d(3, 2, kernel_size=3).to(device)
    result = model(torch.randn(2, 3, 32, 32, device=device))
    result.square().mean().backward()
    assert result.shape == (2, 2, 30, 30)
    assert model.weight.grad is not None
    print("PASS: OpenCV processing and PyTorch forward/backward")


if __name__ == "__main__":
    main()
