FROM ubuntu:latest  
MAINTAINER cuixin <steven.cuixin@gmail.com>  
  
RUN apt-get -y update && \  
apt-get -y install libgoogle-glog-dev libsnappy-dev libprotobuf-dev make git
gcc-4.8 g++ && \  
git clone https://github.com/Qihoo360/pika.git && \  
cd pika && \  
make && \  
cp output/bin/pika /bin && \  
cp output/conf/pika.conf /etc && \  
cd ../ && rm -rf pika && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && \  
mkdir -p /data/log && \  
mkdir -p /data/db && \  
mkdir -p /data/dump && \  
sed -i 's/\.\/log\//\/data\/log/g' /etc/pika.conf && \  
sed -i 's/\.\/db\//\/data\/db/g' /etc/pika.conf && \  
sed -i 's/\.\/dump\//\/data\/dump/g' /etc/pika.conf  
  
EXPOSE 9221  
VOLUME ["/data/"]

