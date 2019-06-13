
python3.6 ./shutdownjava.py 

nohup /usr/local/jdk8/jdk1.8.0_161/bin/java -jar ./daka-0.0.1-SNAPSHOT.jar > javanohup.out 2>&1 &

tail -f ./javanohup.out
#echo '启动java项目'

#/mnt/anaconda3/bin/python3.6 -u /mnt/dakaproject/daka/app.py

#echo '启动python接口'
