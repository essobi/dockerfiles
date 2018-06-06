FROM ubuntu:16.04  
MAINTAINER Kilian Lackhove <kilian@lackhove.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update && apt-get install -y wget xvfb x11vnc supervisor
openjdk-8-jre bzip2  
  
RUN \  
mkdir -p /opt/jbidwatcher \  
&& ver=$(wget https://www.jbidwatcher.com/ -O - | grep -o -P
'JBidwatcher\\-.*?.tar.bz2' | head -n1) \  
&& wget -qO- "https://www.jbidwatcher.com/download/"$ver -P /opt/jbidwatcher/
|\  
tar -jx --strip-components=1 -C /opt/jbidwatcher/  
  
RUN mkdir -p /appdata \  
&& ln -s /appdata ./root/.jbidwatcher  
VOLUME /appdata  
  
EXPOSE 5900  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
CMD ["/usr/bin/supervisord"]  

