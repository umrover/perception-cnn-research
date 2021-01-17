import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.utils.data as data
import cv2

class Detectron2():
    def __init__(self, in_channels):
        super().__init__()
        self.detectron = None # Add Model from the detectron library

    def forward(self, input):
        NotImplemented # Function is dependent both on the nature of the input and the manner in which we need to integrate the libraries

class Yolo():
    def __init__(self, in_channels):
        super().__init__()
    
    def forward(self, input):
        NotImplemented # Function is dependent both on the nature of the input and the manner in which we need to integrate the libraries

