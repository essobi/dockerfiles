FROM ubuntu:14.04  
MAINTAINER Cowboy  
RUN locale-gen en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
ENV LC_CTYPE en_GB.UTF-8  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
RUN apt-get update  
RUN apt-get install -y git build-essential curl wget libpcap-dev clang wget  
# Clone masscan git repo  
RUN wget -q https://github.com/robertdavidgraham/masscan/archive/1.0.3.tar.gz
-O /masscan-1.0.3.tar.gz  
RUN tar xf /masscan-1.0.3.tar.gz -C /opt/ && ln -s /opt/masscan-1.0.3
/opt/masscan && cd /opt/masscan && make -j && cp /opt/masscan/bin/masscan
/usr/local/bin  
WORKDIR /opt/masscan  
ENTRYPOINT ["/usr/local/bin/masscan"]  

