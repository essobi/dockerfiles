FROM verdel/alpine-base:latest  
MAINTAINER Vadim Aleksandrov <valeksandrov@me.com>  
  
ENV FLEXGET_CONF_DIR /etc/flexget  
ENV FLEXGET_SYNC_DIR /sync  
ENV FLEXGET_WEB_PASSWD flexget  
# Install flexget and transmissionrpc  
RUN apk add --update \  
inotify-tools \  
bash \  
&& pip install --upgrade pip \  
&& pip install --upgrade six \  
&& pip install --upgrade pytest-runner \  
&& pip install --upgrade hgtools \  
&& pip install --upgrade flexget \  
&& pip install --upgrade https://github.com/verdel/flexget-lostfilm-
plugin/tarball/master \  
&& pip install transmissionrpc \  
# Clean up  
&& rm -rf \  
/tmp/* \  
/var/cache/apk/*  
  
# Copy init scripts  
COPY rootfs /  
  
ENTRYPOINT ["/init"]

