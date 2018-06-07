FROM ubuntu:16.04  
  
ENV LANG=zh_CN.UTF-8 LANGUAGE=zh_CN.UTF-8 TZ=Asia/Shanghai  
  
#COPY sources.list /etc/apt/sources.list  
  
RUN apt-get update && \  
apt-get -y install curl tzdata unzip && \  
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone &&
\  
dpkg-reconfigure --frontend noninteractive tzdata && \  
groupadd --gid 10000 daily && \  
useradd --uid 10000 -g daily daily && \  
\  
rm -rf /var/lib/apt/lists/* && \  
apt-get clean all  
  

