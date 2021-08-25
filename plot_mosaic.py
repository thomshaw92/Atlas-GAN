import ants
import glob

sub_t1w_filename = glob.glob('*cropped_T1w.nii.gz')[0]
sub_t1w = ants.image_read(sub_t1w_filename)

ants.plot(sub_t1w, axis=1, slices=range(1,100), title=sub_t1w_filename.split('_')[0], filename=f"{sub_t1w_filename.split('_')[0]}_plot.png")