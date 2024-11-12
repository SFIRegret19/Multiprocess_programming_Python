# import multiprocessing
from multiprocessing import Pool
import datetime

def read_info(name):
    all_data = []
    
    with open(name, 'r', encoding='utf-8') as f:
        while f.readline:
            all_data.append(f.readline())

if __name__ == "__main__":
    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]
    # start = datetime.datetime.now()
    # with Pool(processes = len(filenames)) as pl:
    #     result = pl.map_async(read_info, filenames)
    #     # result = pl.imap(read_info, filenames)
    #     # result = pl.map(read_info, filenames)
    # finish = datetime.datetime.now()
    # print(f'{str(finish-start)} (многопроцессный)')

    # start = datetime.datetime.now()
    # for i in filenames:
    #     read_info(i)
    # finish = datetime.datetime.now()
    # print(f' {str(finish - start)} (стандартный)')