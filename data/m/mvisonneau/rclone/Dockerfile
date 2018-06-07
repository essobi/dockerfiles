FROM alpine:latest  
MAINTAINER Maxime VISONNEAU <maxime.visonneau@gmail.com>  
  
ENV RCLONE_VERSION current  
ENV PLATFORM_ARCH amd64  
  
COPY rclone-loop /usr/local/bin/rclone-loop  
  
RUN \  
chmod +x /usr/local/bin/rclone-loop && \  
apk add --no-cache ca-certificates bash && \  
apk add --no-cache --virtual=build-dependencies wget unzip && \  
wget -q
http://downloads.rclone.org/rclone-${RCLONE_VERSION}-linux-${PLATFORM_ARCH}.zip
&& \  
unzip rclone-${RCLONE_VERSION}-linux-${PLATFORM_ARCH}.zip && \  
mv rclone-*-linux-${PLATFORM_ARCH}/rclone /usr/bin && \  
rm -rf rclone-* && \  
apk del --purge build-dependencies  
  
CMD [ "/usr/local/bin/rclone-loop" ]  

