FROM debian:jessie-slim  
MAINTAINER SkaveRat <skaverat@funlynx.de>  
  
RUN apt-get update -qq  
RUN apt-get install curl -qq -y apt-transport-https  
RUN curl --silent http://apt.mopidy.com/mopidy.gpg | apt-key add -  
ADD mopidy.list /etc/apt/sources.list.d/mopidy.list  
RUN apt-get update -qq  
RUN apt-get install -y -qq libjson-glib-dev libao-dev libdbus-glib-1-dev
libnotify-dev libsoup2.4-dev libsox-dev libspotify-dev  
  
COPY lib /usr/lib  
COPY bin /usr/bin  
  
RUN mkdir -p /root/.config/spop  
  
COPY spopd.conf /root/.config/spop/spopd.conf  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/usr/bin/spopd -d"]  

