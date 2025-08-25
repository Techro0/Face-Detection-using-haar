
## Dataset

This project uses **Labeled Faces in the Wild (LFW)**. We do not store the dataset in the repo.  
Download one of these ways:

**Kaggle (recommended):**
```bash
# local
kaggle datasets download -d atulanandjha/lfwpeople -p data --unzip
```
**Colab cell:**
```python
from google.colab import files
files.upload()  # upload kaggle.json
!pip -q install kaggle
!mkdir -p ~/.kaggle && cp kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json
!mkdir -p data
!kaggle datasets download -d atulanandjha/lfwpeople -p data --unzip
```

**Scikit-learn loader (no Kaggle account):**
```python
from sklearn.datasets import fetch_lfw_people
lfw = fetch_lfw_people(data_home="data", funneled=True, resize=0.5, download_if_missing=True)
```
