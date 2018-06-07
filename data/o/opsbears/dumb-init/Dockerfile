FROM opsbears/base:16.04  
RUN apt-get -y install wget && \  
cd /root && \  
wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64.deb && \  
dpkg -i dumb-init_*.deb  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  

