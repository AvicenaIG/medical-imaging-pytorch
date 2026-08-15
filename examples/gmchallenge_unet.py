from collections import defaultdict
import time
import os

import numpy as np

from tqdm import tqdm

from tensorboardX import SummaryWriter

from medicaltorch import datasets as mt_datasets
from medicaltorch import models as mt_models
from medicaltorch import transforms as mt_transforms
from medicaltorch import losses as mt_losses
from medicaltorch import metrics as mt_metrics
from medicaltorch import filters as mt_filters

import torch
from torchvision import transforms
from torch.utils.data import DataLoader
from torch import autograd, optim
import torch.backends.cudnn as cudnn
import torch.nn as nn

import torchvision.utils as vutils

cudnn.benchmark = True


def threshold_predictions(predictions, thr=0.999):
    pass  # TODO: implement


def run_main():
    pass  # TODO: implement






































if __name__ == '__main__':
