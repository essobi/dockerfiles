FROM pataquets/ubuntu  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
exim4 \  
xtail \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD ./exim4.conf /etc/exim4/exim4.conf  
ADD ./start.sh /exim  
  
VOLUME /var/spool/exim4  
  
ENTRYPOINT ["/exim"]  

