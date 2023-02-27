import nibabel as nib
import os
import sys

def progress_bar(progress, x):
    bar_length = 20
    filled_length = int(progress * bar_length)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    percent = int(round(progress * 100))
    status = '\r[{0}] {1}%'.format(bar, percent)
    print("   Splitting file - ", x, end="  ")
    print(status, end='', flush=True)

def count_files(path='.'):
    file_count = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                file_count += 1
            elif entry.is_dir():
                file_count += count_files(entry.path)
    return file_count

data_path = " "  # Define file path of data 
pred_path = "./input/pred"

j = 0

for x in os.listdir(data_path):
    if not x.endswith(".nii") and not x.endswith(".nii.gz"):
        continue
    else:
        img = nib.load(os.path.join(data_path, x))
    # Get the 4D data array
        nii_data = img.get_fdata()

    # Get the dimensions of the 4D data array
        nx, ny, nz, n_vol = nii_data.shape

    # Loop through the volumes and save each as a 3D NIFTI file
        # The loop skips the first baseline image in the NIFTI file
        for i in range(1, n_vol):
        # Extract the i-th 3D volume
            volume_data = nii_data[:, :, :, i]

        # Create a new NIFTI image for the 3D volume
            volume_img = nib.Nifti1Image(volume_data, img.affine)

        # Save the 3D NIFTI file
            save_path = f"{pred_path}/{os.path.splitext(x)[0]}_{i}.nii"
            nib.save(volume_img, save_path)

        # Progress bar
            dir_size = count_files(path=data_path) * (n_vol - 1)
            j = j + 1
            progress_bar(j/dir_size, x)
