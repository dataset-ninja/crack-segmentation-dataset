Dataset **Crack Segmentation Dataset** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/c/s/sN/D5hHLcERvpsMACZSwITnazlHtqWXvrzReg1FuwBWzlA6xEjnCKYUGvp8th59VdFGnT9Rk2k1bwvlgouEO3a0Uw78gPvsSjhVwMuqfvnlLjYA15Xka4d7o3mr7bNu.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Crack Segmentation Dataset', dst_path='~/dtools/datasets/Crack Segmentation Dataset.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/lakshaymiddha/crack-segmentation-dataset/download?datasetVersionNumber=1)