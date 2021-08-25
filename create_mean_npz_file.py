import numpy as np
import SimpleITK as sitk
import os

simg = sitk.ReadImage('/mnt/FileSystem-DeepLearning/tom/Atlas-GAN/EATT_data/average/average.nii.gz')
npy_img = np.zeros([48,80,80])
npy_img[0:47,0:61,0:66] = sitk.GetArrayFromImage(simg)

np.savez_compressed(
    '/mnt/FileSystem-DeepLearning/tom/Atlas-GAN/EATT_data/average/average.npz',
    arr_0=npy_img,
)
