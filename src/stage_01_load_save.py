from src.utils.all_utils import read_yaml, create_directory
import argparse
import pandas as pd
import os
import shutil
from tqdm import tqdm #prints the progress bar

def copy_file(source_download_dir, local_data_dir):
    list_files= os.listdir(source_download_dir)
    N= len(list_files)
    for file in tqdm(list_files, total= N, desc=f'Copying files from {source_download_dir} to {local_data_dir} ', colour="green"):
        src= os.path.join(source_download_dir, file) # from where file is to be copied
        dest= os.path.join(local_data_dir, file) # destination
        shutil.copy(src, dest)

def get_data(config_path):
    config = read_yaml(config_path)

    source_download_dirs = config['source_download_dirs']
    local_data_dirs = config['local_data_dirs']

    for source_download_dir, local_data_dir in tqdm(zip(source_download_dirs, local_data_dirs), total=2, desc='Loading list of folders', colour="red"):
        create_directory([local_data_dir])
        copy_file(source_download_dir, local_data_dir)



if __name__ == '__main__':
    args = argparse.ArgumentParser()

    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    get_data(config_path=parsed_args.config)