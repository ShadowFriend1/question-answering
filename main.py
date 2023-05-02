import matplotlib
from datasets import load_dataset

if __name__ == '__main__':
    ds_openwebtext = load_dataset('openwebtext')
    hendrycks_files = {"auxiliary_train": "aux_train.csv", "test": "test.csv",
                       "validation": "validation.csv", "dev": "dev.csv"}
    ds_hendryckstest = load_dataset('hendrycks_test', data_files=hendrycks_files)
