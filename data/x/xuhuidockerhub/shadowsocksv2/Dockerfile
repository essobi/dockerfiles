FROM ubuntu:trusty  
MAINTAINER Xuhui <1498472791@qq.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PASS **NULL**  
  
RUN apt-get update \  
&& apt-get install -y python-pip \  
&& apt-get install -y python-m2crypto \  
&& apt-get install -y python-dev libevent-dev python-setuptools python-gevent
curl \  
&& easy_install greenlet gevent \  
&& pip install shadowsocks \  
&& mkdir /etc/shadowsocks  
  
COPY Start /Start  
  
EXPOSE 8388  
CMD ["sh","/Start"]  

