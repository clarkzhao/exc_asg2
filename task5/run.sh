#!/bin/bash
hadoop jar /opt/hadoop/hadoop-2.7.3/share/hadoop/tools/lib/hadoop-streaming-2.7.3.jar -D mapred.reduce.tasks=0  -input /data/assignments/ex2/part3/webLarge.txt -output /user/s1682581/assignment2/task5 -mapper mapper.py -file ~/exc_asg2/task5/mapper.py
