FROM pataquets/apache:xenial  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
libapache2-mod-php \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

