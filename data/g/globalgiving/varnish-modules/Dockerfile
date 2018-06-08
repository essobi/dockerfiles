FROM globalgiving/varnish:4.1.3  
MAINTAINER Justin Rupp <jrupp@globalgiving.org>  
  
RUN apt-get update -y && \  
apt-get install -y libvarnishapi-dev=4.1.3-1~jessie pkg-config make wget && \  
cd /tmp && \  
wget https://download.varnish-software.com/varnish-modules/varnish-
modules-0.9.1.tar.gz && \  
tar -xzf varnish-modules-0.9.1.tar.gz && \  
cd varnish-modules-0.9.1 && \  
./configure && \  
make && \  
make install && \  
cd / && \  
apt-get autoremove -y pkg-config make wget && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

