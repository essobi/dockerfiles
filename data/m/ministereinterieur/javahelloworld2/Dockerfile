FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y \  
wget \  
vim  
  
#CMD ping 127.0.0.0 -c 30  
#ENTRYPOINT ["ping", "-c", "50"]  
#CMD ["127.0.0.1"]  
RUN mkdir /data/myvol -p && \  
echo "hello world, a simple java program" > /data/myvol/test  
VOLUME ["/data/myvol"]  

