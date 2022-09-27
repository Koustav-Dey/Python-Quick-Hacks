import time
import tqdm

for i in range(10):
    time.sleep(2)
    print("a")
for i in tqdm.tqdm(range(10)):
    time.sleep(2)