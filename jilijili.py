import requests
import math
import multiprocessing
from multiprocessing import Pool
MAX_WORKER_NUM = multiprocessing.cpu_count()
urls1 = ['https://vod1.627995.com/contents/videos/{}/{}/{}.m3u8'.format(math.floor(i/1000)*1000,i,i) for i in range(99999)]
urls2 = ['https://vod2.627995.com/contents/videos/{}/{}/{}.m3u8'.format(math.floor(i/1000)*1000,i,i) for i in range(99999)]
urls = urls1+urls2
def job(url):
    print(url)
    response = requests.get(url)
    if response.status_code == 200:
        print('夭寿啦，'+url)
        with open('urls.txt','a+', encoding='utf8') as f:
            f.write(url+'\n')
if __name__ == '__main__':

    p = Pool(MAX_WORKER_NUM)
    for url in urls:
        p.apply_async(job, args=(url,))
    p.close()
    p.join()
