
# Dataset: Labeled Faces in the Wild (LFW)

Dataset link (Kaggle): https://www.kaggle.com/datasets/atulanandjha/lfwpeople/data

**Best practice:** do **not** commit the full dataset to the repo. Instead, keep a small `samples/` folder and provide a download script (below). Large files slow down clones and may violate licenses. Use **Git LFS** or **Releases** only if redistribution is permitted.

## Option A — Download via Kaggle API (recommended)

1. Create a Kaggle API Token: Kaggle → *Account* → **Create New API Token**. It downloads `kaggle.json`.
2. **Colab**:
   ```python
   # Upload kaggle.json
   from google.colab import files
   files.upload()  # select kaggle.json

   !mkdir -p ~/.kaggle
   !cp kaggle.json ~/.kaggle/
   !chmod 600 ~/.kaggle/kaggle.json

   # Install Kaggle CLI
   !pip -q install kaggle

   # Download and unzip into data/lfwpeople
   !mkdir -p data
   !kaggle datasets download -d atulanandjha/lfwpeople -p data --unzip
   ```

3. **Local machine** (with Kaggle CLI installed):
   ```bash
   # Place kaggle.json at ~/.kaggle/kaggle.json (chmod 600)
   mkdir -p data
   kaggle datasets download -d atulanandjha/lfwpeople -p data --unzip
   ```

## Option B — Use scikit-learn loader (no Kaggle account needed)
```python
from sklearn.datasets import fetch_lfw_people
lfw = fetch_lfw_people(data_home="data", funneled=True, resize=0.5, download_if_missing=True)
# Images are available at lfw.images, and the raw files are in data/lfw_home or data/lfw_home/lfw_funneled
```
This downloads the official LFW files from the source mirrors.

## Option C — Git LFS or Release Assets (not recommended for full datasets)
If you must include the dataset in GitHub, use **Git LFS**:
```bash
git lfs install
git lfs track "data/**"
git add .gitattributes data/
git commit -m "Track dataset with Git LFS"
git push
```
> Beware of **LFS storage/bandwidth limits** on GitHub.

## Notes
- LFW is widely used for research/education; please respect its terms of use and any redistribution constraints.
- In this repo, we provide *download instructions* rather than mirroring the data.
