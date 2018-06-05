FROM debian:wheezy  
MAINTAINER Dylan Arbour <dylan.arbour@gmail.com>  
  
ENV DEBIAN_FRONTEND="noninteractive"  
# Add Plex PPA  
# https://ilovetechnique.wordpress.com/2013/08/19/installing-plex-media-
server-on-debian/  
RUN apt-get update && apt-get install -y curl && \  
echo "deb http://shell.ninthgate.se/packages/debian wheezy main" \  
>> /etc/apt/sources.list.d/plexmediaserver.list && \  
curl http://shell.ninthgate.se/packages/shell-ninthgate-se-keyring.key | apt-
key add -  
  
# Install Plex  
RUN apt-get update && \  
apt-get -y install plexmediaserver && \  
mkdir /audiovisual && mkdir /plex  
  
# Cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Volumes  
VOLUME /audiovisual  
VOLUME /plex  
  
# Add script for user/group id fix  
ADD init.sh /init.sh  
RUN chmod u+x /init.sh  
  
# Open Plex web port  
EXPOSE 32400  
# Start id fix / Plex  
CMD ["/init.sh"]  

