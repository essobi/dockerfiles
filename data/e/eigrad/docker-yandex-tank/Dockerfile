FROM ubuntu:14.04  
MAINTAINER Andrew Grigorev <andrew@ei-grad.ru>  
  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
  
RUN apt-get update && apt-get -y upgrade  
  
RUN sudo apt-get install -y python python-setuptools && easy_install pip  
  
# instead of add-apt-repository ppa:yandex-load/main  
RUN echo deb http://ppa.launchpad.net/yandex-load/main/ubuntu trusty main >
/etc/apt/sources.list.d/yandex-load-main-trusty.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys CB37D8D1 && \  
apt-get update && apt-get install phantom phantom-ssl  
  
# for psutil, it's sad that they don't have a wheels  
# and for tornado.speedups  
RUN apt-get install -y gcc python-dev  
  
# I need to edit load.ini somehow...  
RUN apt-get install -y vim  
  
COPY yandex-tank /build/  
RUN cd /build && pip install . && cd / && rm -rf /build  
  
COPY yatank-online /build/  
RUN cd /build && pip install . && cd / && rm -rf /build  

