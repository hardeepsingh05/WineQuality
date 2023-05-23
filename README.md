create env

'''bash
conda create -n winesq python=3.7 -y
'''

activate env
'''bash
conda activate wineq
'''

create a requirement.txt 

install the requirements
'''bash
pip install -r requirement.txt


download the dataset from kaggle "wine Quality Dataset"

git init

dvc init

dvc add data _given/winequality.csv

git add .

git commit -m "first commit"
