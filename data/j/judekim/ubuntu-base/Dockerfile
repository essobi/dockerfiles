  
FROM ubuntu:trusty  
  
MAINTAINER judekim "judekim@me.com"  
# Tell Apt never to prompt  
ENV DEBIAN_FRONTEND noninteractive  
  
# this forces dpkg not to call sync() after package extraction and speeds up
install  
RUN echo "force-unsafe-io" > /etc/dpkg/dpkg.cfg.d/02apt-speedup  
  
# we don't need apt cache in a container  
RUN echo "Acquire::http {No-Cache=True;};" > /etc/apt/apt.conf.d/no-cache  
  
# set locale ko_KR  
RUN locale-gen ko_KR ko_KR.UTF-8 \  
&& dpkg-reconfigure locales  
  
RUN apt-get update \  
&& apt-get install -y aptitude \  
&& apt-get clean  
  
RUN aptitude install --without-recommends --assume-yes \  
build-essential \  
ca-certificates \  
curl \  
git \  
htop \  
iputils-ping \  
ssh-client \  
vim \  
&& aptitude clean  
  
# set timezone KST  
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime  
  
ONBUILD RUN aptitude update  

