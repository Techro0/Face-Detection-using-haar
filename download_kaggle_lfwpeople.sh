
#!/usr/bin/env bash
set -euo pipefail

# Download LFW People dataset from Kaggle into data/ (requires Kaggle CLI & kaggle.json)
mkdir -p data
kaggle datasets download -d atulanandjha/lfwpeople -p data --unzip
echo "Done. Files extracted under data/"
