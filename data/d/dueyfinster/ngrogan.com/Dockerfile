FROM alpine:3.4  
MAINTAINER Neil Grogan <neil@grogan.ie>  
  
# set version for s6 overlay  
ARG OVERLAY_VERSION="v1.18.1.5"  
ARG OVERLAY_ARCH="amd64"  
COPY scripts /  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk add \--update curl shadow && \  
./install-hugo.sh && \  
rm /install-hugo.sh && \  
# add s6 overlay  
curl -o \  
/tmp/s6-overlay.tar.gz -L \  
"https://github.com/just-
containers/s6-overlay/releases/download/${OVERLAY_VERSION}/s6-overlay-${OVERLAY_ARCH}.tar.gz"
&& \  
tar xfz \  
/tmp/s6-overlay.tar.gz -C / && \  
# create abc user  
groupmod -g 1000 users && \  
useradd -u 911 -U -d /config -s /bin/false hugo && \  
usermod -G users hugo && \  
chown hugo /root/bin/hugo && \  
chmod 777 /root/bin/hugo  
  
#create dummy site directory and set as working dir  
RUN mkdir /site  
  
WORKDIR /site  
  
# make site a volume  
VOLUME /site  
  
ENTRYPOINT ["/docker_entrypoint.sh"]

