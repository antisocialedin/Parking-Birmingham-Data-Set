import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


def main():
    # Faz a leitura do arquivo
    input_file = '../0-Datasets/bankConvert.csv'
    output_file = '../0-Datasets/bankNormal(min-max).csv'
    names = ['age','job','marital','education','default','balance','housing','loan','duration','previous','poutcome','y']
    features = ['age','job','marital','education','default','balance','housing','loan','duration','previous','poutcome','y']
    target = 'y'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     names = names) # Nome das colunas                      
    ShowInformationDataFrame(df,"Dataframe original")

    # Separating out the features
    x = df.loc[:, features].values
    
    # Separating out the target
    y = df.loc[:,[target]].values

    # Mix-Max normalization
    x_minmax = MinMaxScaler().fit_transform(x)
    normalized2Df = pd.DataFrame(data = x_minmax, columns = features)
    normalized2Df = pd.concat([normalized2Df, df[[target]]], axis = 1)
    ShowInformationDataFrame(normalized2Df,"Dataframe Min-Max Normalized")

    normalized2Df.to_csv(output_file, header=False, index=False)


def ShowInformationDataFrame(df, message=""):
    print(message+"\n")
    print(df.info())
    print(df.describe())
    print(df.head(10))
    print("\n") 

if __name__ == "__main__":
    main()