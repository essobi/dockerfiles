# Dockerfile  
FROM debian:jessie  
MAINTAINER Bin Zhao  
  
# using srouce from aliyun to replace the repo sources  
ADD ./sources.list /etc/apt/sources.list  
  
# set correct timezone  
RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
# update to latest version  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
# setup locale  
apt-get install -y --no-install-recommends locales && \  
echo en_US.UTF-8 UTF-8 > /etc/locale.gen && \  
locale-gen && update-locale LANG=en_US.UTF-8 && \  
# clean up  
apt-get autoremove -y && apt-get clean -y && rm -rf /var/cache/apt/* && rm -rf
/var/lib/apt/lists/*  
  
ENV LANGUAGE en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  

