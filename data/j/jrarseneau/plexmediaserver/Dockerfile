FROM phusion/baseimage:0.9.16  
MAINTAINER J.R. Arseneau <http://github.com/jrarseneau>  
  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
  
# To get rid of error messages like "debconf: unable to initialize frontend:
Dialog":  
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-
selections  
RUN echo "deb http://archive.ubuntu.com/ubuntu trusty multiverse" >>
/etc/apt/sources.list  
  
# Update our image  
RUN apt-get -q update  
RUN apt-get -qy --force-yes dist-upgrade  
  
# Install required packages  
RUN apt-get install -qy avahi-daemon avahi-utils libavahi-client3 wget  
  
# Download and install Plex (non plexpass)  
# Currently static version - will update to dynamic later  
RUN wget -P /tmp https://downloads.plex.tv/plex-media-
server/0.9.12.4.1192-9a47d21/plexmediaserver_0.9.12.4.1192-9a47d21_amd64.deb  
RUN dpkg -i /tmp/plex*.deb  
RUN rm -f /tmp/plex*.deb  
  
EXPOSE 32400  
VOLUME /volumes/config  
VOLUME /volumes/media  
VOLUME /volumes/tmp  
  
RUN mkdir /etc/service/plexmediaserver  
ADD start.sh /etc/service/plexmediaserver/run  
ADD plexmediaserver /etc/default/plexmediaserver  
  
CMD ["/sbin/my_init"]  

