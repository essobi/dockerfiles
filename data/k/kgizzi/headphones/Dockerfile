FROM ubuntu:latest  
MAINTAINER kgizzi <keenan.gizzi@gmail.com>  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y python git-core \  
&& apt-get autoremove \  
&& apt-get clean  
  
VOLUME ["/data"]  
EXPOSE 8181  
WORKDIR /opt  
RUN git clone https://github.com/rembo10/headphones.git  
  
WORKDIR /opt/headphones  
ADD config.ini /tmp/  
ADD start.sh /opt/headphones/  
#CMD /usr/bin/python Headphones.py --config=/data/config.ini --datadir /data  
CMD /opt/headphones/start.sh  

