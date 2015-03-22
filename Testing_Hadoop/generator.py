import time
start_time = time.time()
fo = open("hadoop_test_data.txt", "wb")
for i in range(0,9):
        for i in range(0,10000000):
                fo.write("Hadoop  ");
fo.close()
print("--- %s seconds ---" % (time.time() - start_time))
