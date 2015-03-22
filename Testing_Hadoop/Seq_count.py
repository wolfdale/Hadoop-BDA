import time
start_time = time.time()
file=open("hadoop_test_data.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    print k, v
print("--- %s seconds ---" % (time.time() - start_time))
