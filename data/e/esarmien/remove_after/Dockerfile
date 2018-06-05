FROM ubuntu:14.04  
COPY remove-after.sh /usr/local/bin/remove-after  
RUN \  
apt-get -y update && \  
apt-get -y install curl python && \  
chmod a+x /usr/local/bin/remove-after && \  
curl -sSL https://sdk.cloud.google.com | bash  
CMD ["/usr/local/bin/remove-after"]  

