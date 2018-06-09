# Base image for Docker with the Steam client.  
  
FROM blitznote/debootstrap-amd64:16.04  
MAINTAINER W. Mark Kubacki <wmark@hurrikane.de>  
LABEL org.label-schema.vendor="W. Mark Kubacki" \  
org.label-schema.name="steamcmd packaged" \  
org.label-schema.vcs-type="git" \  
org.label-schema.vcs-url="https://github.com/wmark/docker-steam"  
  
RUN apt-get -q update \  
&& apt-get -y install lib32stdc++6 libcurl3 \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /opt/steam /var/lib/steam \  
&& adduser --disabled-password --no-create-home --gecos 'Steam Client' \--home
/opt/steam steam \  
&& curl --silent --show-error --fail --location --header "Accept:
application/tar+gzip, application/gzip, application/octet-stream" -o - \  
https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz \  
| tar --no-same-owner -xz -C /opt/steam/ \  
&& chown -R steam:steam /opt/steam /var/lib/steam \  
&& chmod 0755 /opt/steam/linux32/steamcmd  
  
USER steam  
WORKDIR /var/lib/steam  
VOLUME /opt/steam/Steam/logs  
  
# this bootstraps the Steam client  
RUN /opt/steam/steamcmd.sh +login anonymous validate +quit  
  
# and this triggers an update  
ONBUILD RUN /opt/steam/steamcmd.sh +login anonymous validate +quit  
  

