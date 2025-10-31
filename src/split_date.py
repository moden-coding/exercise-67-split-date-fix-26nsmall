#!/usr/bin/env python3

from os import sep
import pandas as pd
import numpy as np


def split_date():
    df = pd.read_csv("src\Helsingin_pyorailijamaarat.csv", sep=";")
    Päivämäärä =(df["Päivämäärä"].str.split())
    newdf = pd.DataFrame(Päivämäärä)
    print(newdf)
    
def main():
    split_date()
       
if __name__ == "__main__":
    main()
