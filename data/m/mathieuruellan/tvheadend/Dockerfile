#
-----------------------------------------------------------------------------  
# docker-tvheadend  
#  
#  
# Based on: tobbenb (https://registry.hub.docker.com/u/tobbenb/tvheadend-
unstable/)  
# Updated: 03.02.2015  
# Require: Docker (http://www.docker.io/)  
#
-----------------------------------------------------------------------------  
FROM debian:stretch-slim  
MAINTAINER Mathieu Ruellan <mathieu.ruellan@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV HOME /  
  
  
RUN \  
apt-get update -y && \  
apt-get install -y gnupg2 gnupg dirmngr apt-transport-https && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
379CE192D401AB61  
RUN echo "deb https://dl.bintray.com/tvheadend/deb stretch stable-4.2" | tee
-a /etc/apt/sources.list  
  
RUN \  
apt-get update -y && \  
apt-get install -y tvheadend xmltv xmltv-util udev bzip2 && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD tv_grab_fr_telerama /usr/bin/tv_grab_fr  
RUN chmod a+x /usr/bin/tv_grab_fr  
  
EXPOSE 9981 9982  
VOLUME /config  
VOLUME /recordings  
VOLUME /data  
VOLUME /logos  
VOLUME /timeshift  
VOLUME /.xmltv  
  
ADD entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT /entrypoint.sh  

