import os
import re
import collections

from medicaltorch import transforms as mt_transforms

from tqdm import tqdm
import numpy as np
import nibabel as nib

from torch.utils.data import Dataset
import torch
from torch._six import string_classes, int_classes

from PIL import Image


__numpy_type_map = {
}


class SampleMetadata(object):
    pass  # TODO: implement
    def __init__(self, d=None):
        pass  # TODO: implement

    def __setitem__(self, key, value):
        pass  # TODO: implement

    def __getitem__(self, key):
        pass  # TODO: implement

    def __contains__(self, key):
        pass  # TODO: implement

    def keys(self):
        pass  # TODO: implement


class BatchSplit(object):
    pass  # TODO: implement
    def __init__(self, batch):
        pass  # TODO: implement

    def __iter__(self):
        pass  # TODO: implement


class SegmentationPair2D(object):
    pass  # TODO: implement

    def __init__(self, input_filename, gt_filename, cache=True,
        pass  # TODO: implement








    def get_pair_shapes(self):
        pass  # TODO: implement



    def get_pair_data(self):
        pass  # TODO: implement



    def get_pair_slice(self, slice_index, slice_axis=2):
        pass  # TODO: implement











class MRI2DSegmentationDataset(Dataset):
    pass  # TODO: implement

    def __init__(self, filename_pairs, slice_axis=2, cache=True,
        pass  # TODO: implement


    def _load_filenames(self):
        pass  # TODO: implement

    def _prepare_indexes(self):
        pass  # TODO: implement




    def set_transform(self, transform):
        pass  # TODO: implement


    def compute_mean_std(self, verbose=False):
        pass  # TODO: implement







    def __len__(self):
        pass  # TODO: implement

    def __getitem__(self, index):
        pass  # TODO: implement








class MRI3DSegmentationDataset(Dataset):
    pass  # TODO: implement

    def __init__(self, filename_pairs, cache=True,
        pass  # TODO: implement


    def _load_filenames(self):
        pass  # TODO: implement

    def set_transform(self, transform):
        pass  # TODO: implement


    def __len__(self):
        pass  # TODO: implement

    def __getitem__(self, index):
        pass  # TODO: implement


class MRI3DSubVolumeSegmentationDataset(MRI3DSegmentationDataset):
    pass  # TODO: implement



    def __init__(self, filename_pairs, cache=True,
        pass  # TODO: implement

    def _prepare_indexes(self):
        pass  # TODO: implement



    def __len__(self):
        pass  # TODO: implement

    def __getitem__(self, index):
        pass  # TODO: implement








class DatasetManager(object):
    pass  # TODO: implement
    def __init__(self, dataset, override_transform=None):
        pass  # TODO: implement

    def __enter__(self):
        pass  # TODO: implement

    def __exit__(self, *args):
        pass  # TODO: implement


class SCGMChallenge2DTrain(MRI2DSegmentationDataset):
    pass  # TODO: implement





    def __init__(self, root_dir, slice_axis=2, site_ids=None,
        pass  # TODO: implement










    def _build_train_input_filename(site_id, subj_id, rater_id=None):
        pass  # TODO: implement


class SCGMChallenge2DTest(MRI2DSegmentationDataset):
    pass  # TODO: implement





    def __init__(self, root_dir, slice_axis=2, site_ids=None,
        pass  # TODO: implement






    def _build_train_input_filename(site_id, subj_id, rater_id=None):
        pass  # TODO: implement



def mt_collate(batch):
    pass  # TODO: implement

