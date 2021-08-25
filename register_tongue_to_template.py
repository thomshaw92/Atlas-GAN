ml antspy
import ants as ants
import glob as glob
import numpy as np
import SimpleITK as sitk
import os
#simg = sitk.ReadImage('/mnt/FileSystem-DeepLearning/tom/Atlas-GAN/EATT_data/average/average.nii.gz')
moving_image = ants.image_read('/mnt/FileSystem-DeepLearning/tom/Atlas-GAN/EATT_data/average/path')
fixed_image = ants.image_read('/mnt/FileSystem-DeepLearning/tom/Atlas-GAN/EATT_data/average/path')


ants.registration(fixed, moving, type_of_transform='SyN', initial_transform=None, outprefix='', mask=None, grad_step=0.2, flow_sigma=3, total_sigma=0, aff_metric='mattes', aff_sampling=32, aff_random_sampling_rate=0.2, syn_metric='mattes', syn_sampling=32, reg_iterations=(40, 20, 0), aff_iterations=(2100, 1200, 1200, 10), aff_shrink_factors=(6, 4, 2, 1), aff_smoothing_sigmas=(3, 2, 1, 0), write_composite_transform=False, random_seed=None, verbose=False, multivariate_extras=None, **kwargs)[source]
ants.image_write (object, filename)


template = ants.image_read('template_3T_unimodal/template0.nii.gz')
sub_t1w_filename = glob.glob('sub*/ses*/anat/*T1w.nii.gz')[0]
sub_t1w = ants.image_read(sub_t1w_filename)

print(f"Using {sub_t1w_filename}")

registered_dict = ants.registration(template, sub_t1w, 'SyN')

template_box = ants.image_read('template_3T_unimodal/bounding_box_3T_unimodal.nii.gz')
warped_box = ants.apply_transforms(fixed=sub_t1w, moving=template_box, transformlist= registered_dict['invtransforms'], interpolator='multiLabel', imagetype=0)

#Crop original T1w image
cropped_t1w = ants.crop_image(sub_t1w, label_image=warped_box, label=1)
ants.image_write(cropped_t1w, filename=f"{sub_t1w_filename.split('/')[0]}_cropped_T1w.nii.gz")