# Mostly a clone of timhaak/sabnzbd, but with stuff taken out because wily  
# is less fussy and so am I.  
# My commend line:  
#  
# docker run -d -h <hostname> -v /path/to/config:/config \  
# -v /path/to/data:/data -p 8085:8085 sabnzbd  
FROM ubuntu:wily  
MAINTAINER Dave O Connor <docker@mail.andvari.net>  
  
ENV DEBIAN_FRONTEND="noninteractive"  
RUN echo "deb http://archive.ubuntu.com/ubuntu wily multiverse" >>
/etc/apt/sources.list  
  
RUN apt-get -q update && apt-get -qy --force-yes dist-upgrade  
  
RUN apt-get install -qy sabnzbdplus && apt-get clean  
  
# Should be the same UID on the host.  
RUN useradd --system --uid 2002 -M --shell /usr/bin/nologin media  
  
USER media  
  
# /config should contain your sabnzbd.ini  
# /data is where downloads go. I tned to just have a 'complete' and
'incomplete'  
# dir in there for sab to play with. I use the APi key rather than a watched
directory.  
VOLUME [ "/config", "/data" ]  
  
# Oh, I run it on 8085. For reasons.  
EXPOSE 8085  
  
CMD [ "/usr/bin/sabnzbdplus", "--config-file", "/config/sabnzbd.ini", "--
server", "0.0.0.0:8085", "--console" ]  

