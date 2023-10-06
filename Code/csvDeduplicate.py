import pandas as pd
import glob

outputFile = 'output.csv'

csvList = glob.glob('*.csv')
print(u'共发现%s个CSV文件' % len(csvList))
print(u'processing....')


def mergeCSV():
    for inputFile in csvList:
        print('正在处理：'+inputFile)
        f = open(inputFile)
        data = pd.read_csv(f)
        data.to_csv(outputFile, mode='a', index=False, header=True, encoding='utf-8-sig')
    print('merged!')


def deduplication(file):
    df = pd.read_csv(file, header=0, encoding='utf-8-sig')
    dataList = df.drop_duplicates()
    dataList.to_csv(file, encoding='utf-8-sig')
    print('dedupliated!')


if __name__ == '__main__':
    mergeCSV()
    deduplication(outputFile)
