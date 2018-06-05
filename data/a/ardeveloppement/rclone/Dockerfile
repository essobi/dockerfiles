FROM alpine:3.5  
MAINTAINER CoSpirit Connect <support-arconnect@cospirit.com>  
  
ENV RCLONE_VERSION=current  
ENV ARCH=amd64  
  
RUN apk update \  
&& apk -U add --no-cache ca-certificates fuse openssl \  
&& rm -rf /var/cache/apk/* \  
&& cd /tmp \  
&& wget -q
https://downloads.rclone.org/rclone-${RCLONE_VERSION}-linux-${ARCH}.zip \  
&& unzip /tmp/rclone-${RCLONE_VERSION}-linux-${ARCH}.zip \  
&& mv /tmp/rclone-*-linux-${ARCH}/rclone /usr/bin \  
&& rm -r /tmp/rclone* \  
&& addgroup rclone \  
&& adduser -h /config -s /bin/ash -G rclone -D rclone  
  
USER rclone  
  
VOLUME ["/config", "/data"]  
  
ENTRYPOINT ["/usr/bin/rclone"]  
  
CMD ["--version"]  

