FROM ubuntu:14.04  
MAINTAINER Grant Hutchinson <h.g.utchinson@gmail.com>  
  
ADD ./src /worker/src  
ADD ./docs /worker/docs  
ADD workServer.pro /worker/workServer.pro  
ADD workServer.pro.user /worker/workServer.pro.user  
ADD README.md /worker/README.md  
ADD threadpool_test /worker/threadpool_test  
ADD COPYRIGHT /worker/COPYRIGHT  
  
RUN apt-get update && \  
apt-get install -y git qt5-default qt5-qmake libqt5sql5 libqt5sql5-mysql
libqt5sql5-sqlite libmysqlclient-dev build-essential monit && \  
mkdir /root/.cache/worker2/ -p && \  
cd /worker && \  
sed -i "s/127.0.0.1/0.0.0.0/" /worker/src/server/server.cpp && \  
qmake && make && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 12311  
WORKDIR /worker  
CMD ["/worker/workServer", "-server", "-pass test"]  
  

