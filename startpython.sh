python3.6 ./shutdownpython.py

sleep 20s

echo '启动python项目'

nohup /mnt/anaconda3/bin/python3.6 -u /mnt/dakaproject/daka/app.py > pythonnohup.out 2>&1 &

tail -f ./pythonnohup.out

#echo '启动python接口'
