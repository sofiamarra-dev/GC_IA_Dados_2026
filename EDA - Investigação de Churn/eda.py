import kagglehub
kagglehub.login()

path = kagglehub.dataset_download("blastchar/telco-customer-churn")
print("Path to dataset files:", path)

import pandas as pd 
import os

# lista os arquivos baixados
arquivos =(os.listdir(path))
print(arquivos)

# carrega o CSV
df = pd.read_csv(os.path.join(path,'WA_Fn-UseC_-Telco-Customer-Churn.csv'))

df.head(10)