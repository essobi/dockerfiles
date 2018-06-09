FROM alpine:3.7  
MAINTAINER Chris Kankiewicz <Chris@ChrisKankiewicz.com>  
  
# Define transmission-daemon version  
ARG TD_VERSION=2.92-r8  
  
# Create directories  
RUN mkdir -pv /etc/transmission-daemon/blocklists /srv/downloads/.incomplete
/srv/watchdir  
  
# Add settings file  
COPY files/settings.json /etc/transmission-daemon/settings.json  
  
# Install packages and dependencies  
RUN apk add --update curl transmission-cli transmission-daemon=${TD_VERSION}
tzdata \  
&& rm -rf /var/cache/apk/*  
  
# Install initial blocklist  
ARG
BLOCKLIST_URL="http://list.iblocklist.com/?list=bt_level1&fileformat=p2p&archiveformat=gz"  
RUN curl -sL ${BLOCKLIST_URL} | gunzip > /etc/transmission-
daemon/blocklists/bt_level1  
  
# Create bolcklist-update cronjob  
COPY files/blocklist-update /etc/periodic/hourly/blocklist-update  
RUN chmod +x /etc/periodic/hourly/blocklist-update  
  
# Add docker volumes  
VOLUME /etc/transmission-daemon  
  
# Expose ports  
EXPOSE 9091 51413  
# Run transmission-daemon as default command  
CMD ["transmission-daemon", "--foreground", "--log-info", "--config-dir",
"/etc/transmission-daemon"]  

