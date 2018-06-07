FROM debian:8  
MAINTAINER lacsap  
  
# Requirements installation  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
git \  
build-essential \  
nodejs \  
python  
  
# Getting CJDNS  
RUN mkdir -p /usr/src  
RUN git clone https://github.com/cjdelisle/cjdns.git /usr/src/cjdns  
  
WORKDIR /usr/src/cjdns  
RUN ./do  
  
# Installing CJDNS  
RUN install -m755 -oroot -groot /usr/src/cjdns/cjdroute /usr/bin/cjdroute  
RUN mkdir -p /etc/cjdns  
  
COPY entry.sh /entry.sh  
VOLUME ["/etc/cjdns"]  
ENTRYPOINT ["/bin/bash", "/entry.sh"]  

