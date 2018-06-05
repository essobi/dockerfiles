FROM ubuntu:14.04  
MAINTAINER Tuomas Suutari <tuomas.suutari@gmail.com>  
RUN \  
apt-get update -y && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y socat && \  
rm -fr /var/lib/apt/lists/*  
ADD run.sh /run.sh  
CMD ["/run.sh"]  

