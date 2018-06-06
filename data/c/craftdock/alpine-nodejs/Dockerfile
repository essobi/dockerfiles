# NodeJs apk builder  
FROM craftdock/apk-nodejs:current as nodejs_apk_builder  
  
ENV PACKAGER "Hexosse <hexosse@gmail.com>"  
RUN set -x \  
# Build Hugo apk file  
&& /entrypoint abuild -r -P /packages \  
# Copy packages outside of builder volume  
&& sudo cp -r /packages /tmp/nodejs  
  
  
  
# NodeJs  
FROM craftdock/alpine-runit:latest  
  
LABEL maintainer="Hexosse <hexosse@gmail.com>" \  
description="Minimal Alpine image with NodeJs and Yarn."  
  
COPY \--from=nodejs_apk_builder /tmp/nodejs /tmp/nodejs  
  
# Install node  
RUN \  
# Print executed commands  
set -x \  
# Update repository indexes  
&& apk-update \  
# NodeJs need libuv >= 1.18.0 and http-parser  
&& apk-install --repository http://dl-cdn.alpinelinux.org/alpine/edge/main/
libuv http-parser \  
# Install NodeJs  
&& apk-install --repository /tmp/nodejs --allow-untrusted nodejs nodejs-npm \  
# Install Yarn  
&& apk-install --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ yarn \  
# Clear apk's cache  
&& apk-cleanup  
  
# Copy scripts  
COPY ./rootfs /  

