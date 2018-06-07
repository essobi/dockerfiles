FROM odise/busybox-python:stable  
MAINTAINER Johan Stenqvist <johan@stenqvist.net>  
LABEL Description="Dockerized dropbox"  
RUN adduser -h /dropbox -s /bin/sh -D dropbox users \  
&& install -dm0 /dropbox/.dropbox-dist  
ARG dropbox_version=8.4.21  
RUN curl -L "https://d1ilhw0800yew8.cloudfront.net/client/dropbox-
lnx.x86_64-${dropbox_version}.tar.gz" \  
| gunzip -c - | tar -xf - -C /tmp \  
&& mv /tmp/.dropbox-dist /opt/dropbox \  
&& rm -rf /tmp/*  
USER dropbox  
CMD ["/opt/dropbox/dropboxd"]  

