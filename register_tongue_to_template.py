#run in singularity shell of docker://stnava/antspy:latest
import ants as ants
import glob as glob
import os

template = ants.image_read('/home/opc/vnm/tom/EATT_tongue_data/template/template0.nii.gz')
sub_t1w_filename = glob.glob('*T1w.nii.gz')[0]
sub_t1w = ants.image_read(sub_t1w_filename)

print(f"Using {sub_t1w_filename}")

#register
registered_t1 = ants.registration(template, sub_t1w, 'Similarity')
#use better interpolation
warped_t1_good_interp = ants.apply_transforms(fixed=template, moving=sub_t1w, transformlist= registered_t1['fwdtransforms'], interpolator='hammingWindowedSinc', imagetype=0)

template_box = ants.image_read('/home/opc/vnm/tom/EATT_tongue_data/template/resliced_tongue_bounding_box.nii.gz')
cropped_t1w_template_space = ants.crop_image(warped_t1_good_interp, label_image=template_box, label=1)

#Crop original T1w image
#cropped_t1w = ants.crop_image(sub_t1w, label_image=warped_box, label=1)
ants.image_write(cropped_t1w_template_space, filename=f"{sub_t1w_filename.split('_')[0]}_cropped_T1w.nii.gz")