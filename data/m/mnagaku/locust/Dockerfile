FROM ubuntu:trusty  
  
MAINTAINER mnagaku <mnagaku@gmail.com>  
  
RUN echo "Asia/Tokyo" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata && locale-gen en_US.UTF-8 && update-locale LANG=en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C  
ENV LC_ALL en_US.UTF-8  
RUN sed -i".bak" -e 's/\/\/archive.ubuntu.com/\/\/ftp.jaist.ac.jp/g'
/etc/apt/sources.list &&\  
apt-get update &&\  
apt-get upgrade -y &&\  
apt-get install -y build-essential python-dev python-pip python-pycurl wget
&&\  
pip install pyzmq &&\  
pip install locustio  
  
EXPOSE 5557  
EXPOSE 5558  
EXPOSE 8089  
CMD tail -f /dev/null  

