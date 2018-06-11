# Etcd  
# ====  
#  
# Build:  
#  
# docker built -t waitingkuo/etcd .  
#  
# Run:  
#  
# docker run -d -p 4001:4001 -p 7001:7001 waitingkuo/etcd  
#  
# VERSION 0.1  
FROM ubuntu:latest  
MAINTAINER waitingkuo0527@gmail.com  
  
  
# Install Prerequisites  
RUN apt-get update  
RUN apt-get install -y python-software-properties git  
  
# Install GOLANG  
RUN add-apt-repository -y ppa:duh/golang  
RUN apt-get update  
RUN apt-get install -y golang  
  
RUN apt-get install git  
  
# Install etcd  
#RUN git clone git@github.com:coreos/etcd.git  
RUN mkdir -p /opt  
RUN cd /opt && git clone https://github.com/coreos/etcd.git  
RUN cd /opt/etcd && ./build  
  
# Expose Ports  
EXPOSE 4001 7001  
ENTRYPOINT ["/opt/etcd/etcd"]  

