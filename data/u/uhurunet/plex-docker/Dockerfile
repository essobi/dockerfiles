############################################################  
# Dockerfile to build Plex Installed Containers  
# Based on Fedora 21  
############################################################  
  
FROM uhurunet/fedora21  
MAINTAINER Frederick Mbuya "freddie@uhurunet.com"  
  
RUN yum -y update  
ADD plexaa /tmp/plexaa  
ADD plexab /tmp/plexab  
ADD plexac /tmp/plexac  
RUN cat /tmp/plexa* > /tmp/plexmediaserver-0.9.11.7.803-87d0708.x86_64.rpm  
RUN yum -y install /tmp/plexmediaserver-0.9.11.7.803-87d0708.x86_64.rpm  
ADD supervisord.conf /etc/supervisord.conf  
  
EXPOSE 22 32400  
#ENTRYPOINT ["/usr/bin/supervisord"]  
ENTRYPOINT ["/bin/bash"]  

