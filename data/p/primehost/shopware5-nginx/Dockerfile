FROM primehost/nginx  
MAINTAINER Prime-Host <info@nordloh-webdesign.de>  
  
# update before install  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# clean up unneeded packages  
RUN apt-get \--purge autoremove -y  
  
# Custom nginx conf for Shopware  
ADD ./nginx-default.conf /etc/nginx/sites-available/default  
  
# Shopware Initialization and Startup Script  
ADD ./shopware5-start.sh /root/container-scripts/prime-host/shopware5-start.sh  
RUN chmod 755 /root/container-scripts/prime-host/shopware5-start.sh  
  
CMD ["/bin/bash", "/root/container-scripts/prime-host/shopware5-start.sh"]  

