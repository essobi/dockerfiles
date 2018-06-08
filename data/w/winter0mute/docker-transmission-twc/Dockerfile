# Inspiration from the phlak/transmission image  
# DockerHub: https://hub.docker.com/r/phlak/transmission/  
# GitHub: https://github.com/PHLAK/docker-transmission  
FROM alpine:3.6  
MAINTAINER winter0mute <winter0mute@noreply.net>  
  
LABEL Description="Run as (adjust volume paths/ports/TZ/image name/container
name): docker run -d -v transmission-data:/etc/transmission-daemon:Z -v
/local/downloads:/srv/downloads:Z -p 9091:9091 -p 51413:51413/udp -e
TZ=Europe/Budapest --name transmission winter0mute/transmission-daemon"  
  
# Create directories  
RUN mkdir -pv /etc/transmission-daemon/blocklists /srv/downloads/.incomplete
/srv/watchdir  
  
# Add settings file  
COPY files/settings.json /etc/transmission-daemon/settings.json  
  
# Install packages and dependencies  
RUN apk add --update curl transmission-cli transmission-daemon tzdata \  
&& apk add ca-certificates wget \  
&& update-ca-certificates \  
&& rm -rf /var/cache/apk/*  
  
# Install initial blocklist  
RUN curl -sL
"http://list.iblocklist.com/?list=bt_level1&fileformat=p2p&archiveformat=gz" |
gunzip > /etc/transmission-daemon/blocklists/bt_level1  
  
# Create bolcklist-update cronjob  
COPY files/blocklist-update /etc/periodic/hourly/blocklist-update  
RUN chmod +x /etc/periodic/hourly/blocklist-update  
  
# Copy entrypoint  
COPY files/entrypoint.sh /root/entrypoint.sh  
RUN chmod +x /root/entrypoint.sh  
  
# Install transmission-web-control (https://github.com/ronggang/transmission-
web-control)  
ADD https://raw.githubusercontent.com/ronggang/transmission-web-
control/master/release/install-tr-control.sh /tmp  
RUN echo 1 | sh /tmp/install-tr-control.sh \  
&& rm /tmp/install-tr-control.sh  
  
# Expose ports  
EXPOSE 9091 51413  
# Run transmission-daemon as default command  
CMD ["/root/entrypoint.sh"]  
  

