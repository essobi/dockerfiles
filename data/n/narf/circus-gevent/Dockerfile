FROM ubuntu:trusty  
MAINTAINER Nat Lownes <nat.lownes@gmail.com>  
  
RUN apt-get update -qq -y  
RUN apt-get install -y imagemagick  
RUN apt-get install -y imagemagick-common  
RUN apt-get install -y python2.7  
RUN apt-get install -y python-pip  
RUN apt-get install -y python-virtualenv  
RUN apt-get install -y libzmq-dev  
RUN apt-get install -y libevent-dev  
RUN apt-get install -y python-dev  
  
RUN pip install circus  
RUN pip install circus-web  
RUN pip install chaussette  
RUN pip install gevent  
  
RUN useradd -d /home/web -m -s /bin/bash web  
RUN chown -R web /home/web  
  
WORKDIR /home/web  
USER  web  
RUN mkdir -p /home/web/virtualenvs  

