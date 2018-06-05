# davical:tool  
FROM janlo/davical  
  
MAINTAINER Jan Losinski <losinski@wh2.tu-dresden.de>  
  
RUN apt-get update && \  
apt-get -y install --no-install-recommends \  
postgresql-client && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD init_davical.sh /usr/local/bin/init_davical.sh  
  
CMD ["/usr/local/bin/init_davical.sh"]  

