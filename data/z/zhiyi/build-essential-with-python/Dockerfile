FROM ubuntu:latest  
MAINTAINER zhiyi liu <liuzhiyi@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
#Only for Chinese user  
RUN apt-get -qq update && \  
apt-get -qqy install --no-install-recommends \  
build-essential python &&\  
rm -rf /var/lib/apt/lists/* &&\  
mkdir -p /root/build  
ADD start.sh /start.sh  
  
VOLUME ["/mnt"]  
CMD ["sh", "/start.sh"]  
  

