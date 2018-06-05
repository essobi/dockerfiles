FROM akihirosuda/zookeeper-dynamic  
MAINTAINER akihirosuda  
  
RUN apt-get update && apt-get install -y telnet netcat lv less vim python-
colorama  
RUN mkdir /zk01_log /zk02_log  
ADD zk01_conf.ORIG /zk01_conf.ORIG  
ADD zk02_conf.ORIG /zk02_conf.ORIG  
ADD zk01_data.ORIG /zk01_data.ORIG  
ADD zk02_data.ORIG /zk02_data.ORIG  
ADD init.py /  
WORKDIR /  
CMD ["python", "/init.py"]  

