FROM ubuntu:14.04  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -y -q install python-software-properties software-properties-common &&
\  
add-apt-repository ppa:yandex-load/main && \  
apt-get update && \  
apt-get -y -q install yandex-tank && \  
apt-get -y remove python-software-properties software-properties-common && \  
apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT /usr/bin/yandex-tank  

