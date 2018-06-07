FROM ubuntu:16.04  
MAINTAINER Florin Patan  
  
EXPOSE 4567  
ENV KINESALITE_VERSION=1.11.6  
RUN apt-get update && apt-get install -y g++ \  
make \  
python \  
software-properties-common \  
wget  
RUN wget -qO- https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get update && \  
apt-get install -y nodejs  
RUN wget -O kinesalite.tar.gz
https://github.com/mhart/kinesalite/archive/v${KINESALITE_VERSION}.tar.gz && \  
tar -xf kinesalite.tar.gz -C /tmp/ && \  
rm -f /tmp/kinesalite.tar.gz  
WORKDIR /tmp/kinesalite  
RUN npm install -g kinesalite && \  
apt-get purge -y g++ \  
make \  
software-properties-common \  
wget && \  
apt-get -y autoremove && \  
apt-get clean && rm -rf /build && rm -rf /tmp/* /var/tmp/* && rm -rf
/var/lib/apt/lists/*  
  
CMD ["/usr/bin/kinesalite","--createStreamMs=100","--deleteStreamMs=100","--
updateStreamMs=100"]  

