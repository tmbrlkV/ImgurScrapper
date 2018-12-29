import sys
import os
from threading import Thread

from scrapper import Scrapper

def scrap_pictures(scrapper):
    while True:
        img = scrapper.generate_random_url()
        scrapper.scrape(img)

if __name__ == '__main__':
    path = sys.argv[1] if len(sys.argv) > 1 else None
    thread_count = int(sys.argv[2]) if len(sys.argv) > 2 else 1

    if not os.path.exists(path):
        os.makedirs(path)

    picture_scrapper = Scrapper(path)
    threads = []

    try:
        for _ in range(thread_count):
            thread = Thread(target = scrap_pictures, args = (picture_scrapper,))
            thread.start()
            threads.append(thread)
    except KeyboardInterrupt:
        for t in threads:
            t.join(1)
