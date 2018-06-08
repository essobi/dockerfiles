FROM ubuntu:14.04  
MAINTAINER Mirs King <mirsking@gmail.com>  
  
# change the default ros source list  
RUN rm -f /etc/apt/sources.list  
RUN echo " \n \  
deb http://mirrors.ustc.edu.cn/ubuntu/ trusty main restricted universe
multiverse \n \  
deb http://mirrors.ustc.edu.cn/ubuntu/ trusty-security main restricted
universe multiverse \n \  
deb http://mirrors.ustc.edu.cn/ubuntu/ trusty-updates main restricted universe
multiverse \n \  
deb http://mirrors.ustc.edu.cn/ubuntu/ trusty-proposed main restricted
universe multiverse \n \  
deb http://mirrors.ustc.edu.cn/ubuntu/ trusty-backports main restricted
universe multiverse \n \  
deb-src http://mirrors.ustc.edu.cn/ubuntu/ trusty main restricted universe
multiverse \n \  
deb-src http://mirrors.ustc.edu.cn/ubuntu/ trusty-security main restricted
universe multiverse \n \  
deb-src http://mirrors.ustc.edu.cn/ubuntu/ trusty-updates main restricted
universe multiverse \n \  
deb-src http://mirrors.ustc.edu.cn/ubuntu/ trusty-proposed main restricted
universe multiverse \n \  
deb-src http://mirrors.ustc.edu.cn/ubuntu/ trusty-backports main restricted
universe multiverse \n \  
" > /etc/apt/sources.list  
  
# common apps  
RUN apt-get -y update \  
&& apt-get install wget curl openssh-server locate \  
software-properties-common \  
git mercurial -y  

