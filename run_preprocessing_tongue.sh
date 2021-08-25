#!/bin/bash

if [[ ! -e /mnt/FileSystem-DeepLearning/tom/Atlas-GAN/subjnames_EATT.csv ]] ; then
    cd ~/vnm/tom/EATT_tongue_data/T1s_N4_denoised_wholebrain/
    for sub in sub*gz ; do 
        echo ${sub:0:6} >> /mnt/FileSystem-DeepLearning/tom/Atlas-GAN/subjnames_EATT.csv 
    done
fi

singularity="singularity exec -B /mnt/:/mnt /mnt/FileSystem-DeepLearning/tom/Atlas-GAN/antspy_latest.sif"

for subjName in `cat /mnt/FileSystem-DeepLearning/tom/Atlas-GAN/subjnames_EATT.csv ` ; do
    echo ${subjName}
    mkdir -p "/home/opc/vnm/tom/tmpdir/${subjName}"
    tmpdir="/home/opc/vnm/tom/tmpdir/${subjName}"
    cd ${tmpdir}
    cp /home/opc/vnm/tom/EATT_tongue_data/T1s_N4_denoised_wholebrain/${subjName}_N4BiasFieldCorrected_Denoised_T1w.nii.gz ${tmpdir}/
    ${singularity} python /mnt/FileSystem-DeepLearning/tom/Atlas-GAN/register_tongue_to_template.py
    ${singularity} python /mnt/FileSystem-DeepLearning/tom/Atlas-GAN/plot_mosaic.py
    cp ${tmpdir}/* /home/opc/vnm/tom/EATT_tongue_data/T1s_N4_denoised_wholebrain/
    #rm -r ${tmpdir}
done