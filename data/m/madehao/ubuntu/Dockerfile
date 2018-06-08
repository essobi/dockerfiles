FROM ubuntu:16.04  
  
MAINTAINER madehao1983@sina.com  
  
ENV TZ="Asia/Shanghai"  
RUN set -x \  
&& apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install tzdata \  
&& ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& echo "Asia/Shanghai" > /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata  

