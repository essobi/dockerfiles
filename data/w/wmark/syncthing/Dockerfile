FROM blitznote/baseimage  
MAINTAINER W. Mark Kubacki <wmark@hurrikane.de>  
LABEL org.label-schema.vendor="W. Mark Kubacki" \  
org.label-schema.name="directory synchronization deamon (like rsync, unison)"
\  
org.label-schema.vcs-type="git" \  
org.label-schema.vcs-url="https://github.com/wmark/docker-syncthing"  
  
COPY bootstrap.sh default-config.xml /  
COPY chpst /usr/bin/  
  
RUN chmod a+x /usr/bin/chpst \  
&& mkdir /home/syncthing \  
&& curl --silent --show-error --fail --location --header "Accept:
application/tar+gzip, application/x-gzip, application/octet-stream" \  
$(curl --silent --show-error --fail --location --header 'Accept:
application/json' \  
https://api.github.com/repos/syncthing/syncthing/releases/latest \  
| jq -r '.assets[] | select(.name | contains("linux")) | select(.name |
contains("amd64")) | select(.browser_download_url | contains(".tar")) |
.browser_download_url') \  
| tar --no-same-owner --strip-components=1 --wildcards -C /home/syncthing -xz
"*/syncthing" \  
&& chmod 0755 /home/syncthing/syncthing \  
&& sha256sum /home/syncthing/syncthing \  
&& /home/syncthing/syncthing -version  
  
WORKDIR /home/syncthing  
  
EXPOSE 8080 22000 21025/udp  
VOLUME /home/syncthing/.config/syncthing /home/syncthing/Sync  
  
ENTRYPOINT ["/bin/bash", "/bootstrap.sh",
"-home=/home/syncthing/.config/syncthing", "-gui-address=[::]:8080"]  

