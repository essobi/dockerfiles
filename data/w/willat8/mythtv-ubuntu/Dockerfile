FROM ubuntu:artful  
  
RUN apt-get update && \  
apt-get upgrade -y  
  
RUN apt-get install -y mythtv-backend  
  
RUN apt-get install -y locales iputils-ping && \  
locale-gen "en_AU.UTF-8" && \  
dpkg-reconfigure \--frontend=noninteractive locales && \  
ln -sfv /usr/share/zoneinfo/Australia/Sydney /etc/localtime  
  
ENV LC_ALL=en_AU.UTF-8 \  
LANG=en_AU.UTF-8  
  
ENTRYPOINT ["mythbackend"]  
  

