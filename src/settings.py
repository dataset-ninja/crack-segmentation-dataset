from typing import Dict, List, Optional, Union

from dataset_tools.templates import (
    AnnotationType,
    Category,
    CVTask,
    Domain,
    Industry,
    License,
    Research,
)

##################################
# * Before uploading to instance #
##################################
PROJECT_NAME: str = "Crack Segmentation Dataset"
PROJECT_NAME_FULL: str = "Crack Segmentation Dataset"

##################################
# * After uploading to instance ##
##################################
LICENSE: License = License.Custom(url="Unknown")
APPLICATIONS: List[Union[Industry, Domain, Research]] = [Industry.Utilities(is_used=False)]
CATEGORY: Category = Category.EnergyAndUtilities(extra=Category.Safety(), is_original_dataset=False)

CV_TASKS: List[CVTask] = [CVTask.SemanticSegmentation()]
ANNOTATION_TYPES: List[AnnotationType] = [AnnotationType.SemanticSegmentation()]


RELEASE_DATE: Optional[str] = None  # e.g. "YYYY-MM-DD"
if RELEASE_DATE is None:
    RELEASE_YEAR: int = 2020

HOMEPAGE_URL: str = "https://www.kaggle.com/datasets/lakshaymiddha/crack-segmentation-dataset"
# e.g. "https://some.com/dataset/homepage"

PREVIEW_IMAGE_ID: int = 1662678
# This should be filled AFTER uploading images to instance, just ID of any image.

GITHUB_URL: str = "https://github.com/dataset-ninja/crack-segmentation-dataset"
# URL to GitHub repo on dataset ninja (e.g. "https://github.com/dataset-ninja/some-dataset")

##################################
### * Optional after uploading ###
##################################
DOWNLOAD_ORIGINAL_URL: Optional[
    Union[str, dict]
] = "https://www.kaggle.com/datasets/lakshaymiddha/crack-segmentation-dataset/download?datasetVersionNumber=1"
# Optional link for downloading original dataset (e.g. "https://some.com/dataset/download")

CLASS2COLOR: Optional[Dict[str, List[str]]] = None
# If specific colors for classes are needed, fill this dict (e.g. {"class1": [255, 0, 0], "class2": [0, 255, 0]})

PAPER: Optional[Union[str, List[str]]] = [
    "https://ieeexplore.ieee.org/abstract/document/7533052",
    "https://ieeexplore.ieee.org/abstract/document/8694955",
    "https://ieeexplore.ieee.org/abstract/document/7966101",
    "https://ieeexplore.ieee.org/abstract/document/7471507",
    "https://ieeexplore.ieee.org/abstract/document/7572082",
    "https://www.sciencedirect.com/science/article/abs/pii/S0167865511003795",
    "https://www.researchgate.net/profile/Liang-Yang-52/publication/319333841_Deep_Concrete_Inspection_Using_Unmanned_Aerial_Vehicle_Towards_CSSC_Database/links/59e0e27a458515393d4ed035/Deep-Concrete-Inspection-Using-Unmanned-Aerial-Vehicle-Towards-CSSC-Database.pdf",
    "https://www.sciencedirect.com/science/article/abs/pii/S0925231219300566",
]
CITATION_URL: Optional[
    str
] = "https://www.kaggle.com/datasets/lakshaymiddha/crack-segmentation-dataset"
AUTHORS: Optional[List[str]] = [
    "Zhang, Lei",
    "Yang, Fan",
    "Zhang, Yimin Daniel",
    "Zhu, Ying Julie",
    "Yang, Fan",
    "Zhang, Lei",
    "Yu, Sijia",
    "Prokhorov, Danil",
    "Mei, Xue",
    "Ling, Haibin",
    "Eisenbach, Markus",
    "Stricker, Ronny",
    "Seichter, Daniel",
    "Amende, Karl",
    "Debes, Klaus",
    "Sesselmann, Maximilian",
    "Ebersbach, Dirk",
    "Stoeckert, Ulrike",
    "Gross, Horst-Michael",
    "Shi, Yong",
    "Cui, Limeng",
    "Qi, Zhiquan",
    "Meng, Fan",
    "Chen, Zhensong",
    "Amhaz, Rabih",
    "Chambon, Sylvie",
    "Idier, Jérôme",
    "Baltazart, Vincent",
    "Zou, Qin",
    "Cao, Yu",
    "Li, Qingquan",
    "Mao, Qingzhou",
    "Wang, Song",
    "Liu, Yahui",
    "Yao, Jian",
    "Lu, Xiaohu",
    "Xie, Renping",
    "Li, Li",
    "Liang Yang",
    "Bing Li",
    "Wei Li",
    "Zhaoming Liu",
    "Guoyong Yang",
    "Jizhong Xiao",
    "Lakshay Middha",
]

ORGANIZATION_NAME: Optional[Union[str, List[str]]] = None
ORGANIZATION_URL: Optional[Union[str, List[str]]] = None

SLYTAGSPLIT: Optional[Dict[str, List[str]]] = None
TAGS: List[str] = None

##################################
###### ? Checks. Do not edit #####
##################################


def check_names():
    fields_before_upload = [PROJECT_NAME]  # PROJECT_NAME_FULL
    if any([field is None for field in fields_before_upload]):
        raise ValueError("Please fill all fields in settings.py before uploading to instance.")


def get_settings():
    if RELEASE_DATE is not None:
        global RELEASE_YEAR
        RELEASE_YEAR = int(RELEASE_DATE.split("-")[0])

    settings = {
        "project_name": PROJECT_NAME,
        "license": LICENSE,
        "applications": APPLICATIONS,
        "category": CATEGORY,
        "cv_tasks": CV_TASKS,
        "annotation_types": ANNOTATION_TYPES,
        "release_year": RELEASE_YEAR,
        "homepage_url": HOMEPAGE_URL,
        "preview_image_id": PREVIEW_IMAGE_ID,
        "github_url": GITHUB_URL,
    }

    if any([field is None for field in settings.values()]):
        raise ValueError("Please fill all fields in settings.py after uploading to instance.")

    settings["release_date"] = RELEASE_DATE
    settings["project_name_full"] = PROJECT_NAME_FULL or PROJECT_NAME
    settings["download_original_url"] = DOWNLOAD_ORIGINAL_URL
    settings["class2color"] = CLASS2COLOR
    settings["paper"] = PAPER
    settings["citation_url"] = CITATION_URL
    settings["authors"] = AUTHORS
    settings["organization_name"] = ORGANIZATION_NAME
    settings["organization_url"] = ORGANIZATION_URL
    settings["slytagsplit"] = SLYTAGSPLIT
    settings["tags"] = TAGS

    return settings
