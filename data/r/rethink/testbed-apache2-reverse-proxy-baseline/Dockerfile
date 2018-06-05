# docker image for a baseline installation of a reverse proxy  
# using apache2 virtual hosts functionality.  
#  
# this docker images provides everythink except the configuration  
# of the actual reverse proxying (virtual hosts config)  
#  
FROM rethink/testbed-baseline  
  
MAINTAINER marc.emmelmann@fokus.fraunhofer.de  
  
RUN apt-get update -y && apt-get install -y apache2 apache2-doc  
RUN apt-get update -y && apt-get install -y libapache2-mod-proxy-html  
  
RUN a2enmod proxy  
RUN a2enmod proxy_html  
RUN a2enmod proxy_http  
  
  
  
RUN cd /opt/reTHINK && echo "/opt/reTHINK provided by rethink/testbed-baseline
docker image ... yes"  
  
ENTRYPOINT /etc/init.d/apache2 restart && echo "Started apache2 deamon for
reverse proxing in the background\n String bash now" && /bin/bash  
  
  

