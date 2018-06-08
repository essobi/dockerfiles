FROM ubuntu:14.04  
MAINTAINER Dominique Barton  
  
#  
# Create user and group for Plex.  
#  
RUN groupadd -r -g 666 plex \  
&& useradd -r -u 666 -g 666 plex  
  
#  
# Install Plex and all required dependencies.  
#  
RUN export VERSION=1.13.2.5102-4898d7d96 \  
&& apt-get -q update \  
&& apt-get install -qy curl gdebi-core \  
&& apt-get remove -qy udev \  
&& curl -o /tmp/plexmediaserver_amd64.deb https://downloads.plex.tv/plex-
media-server/${VERSION}/plexmediaserver_${VERSION}_amd64.deb \  
&& gdebi -n /tmp/plexmediaserver_amd64.deb \  
&& apt-get -y remove curl gdebi-core \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/*  
  
#  
# Add required files for plex.  
#  
ADD plex.sh /plex.sh  
RUN chmod 755 /plex.sh  
  
ADD default /etc/default/plexmediaserver  
RUN chmod 644 /etc/default/plexmediaserver  
  
ADD init.override /etc/init/plexmediaserver.override  
RUN chmod 644 /etc/init/plexmediaserver.override  
  
#  
# Define container settings.  
#  
VOLUME ["/config", "/transcode", "/media"]  
  
EXPOSE 32400  
#  
# Start Plex Media Server.  
#  
WORKDIR /config  
CMD ["/plex.sh"]  

