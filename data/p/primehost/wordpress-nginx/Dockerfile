FROM primehost/nginx  
MAINTAINER Kevin Nordloh <mail@legendary-server.de>  
  
# update before install  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# clean up unneeded packages  
RUN apt-get \--purge autoremove -y  
  
# Wordpress Initialization and Startup Script  
ADD ./wordpress-start.sh /root/container-scripts/prime-host/wordpress-start.sh  
RUN chmod 755 /root/container-scripts/prime-host/wordpress-start.sh  
  
CMD ["/bin/bash", "/root/container-scripts/prime-host/wordpress-start.sh"]  

