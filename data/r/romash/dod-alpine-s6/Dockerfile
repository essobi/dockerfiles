FROM alpine:edge  
MAINTAINER Romash <tcp6000@gmail.com>  
  
# global variables, will be available in any heritable images  
ENV TERM="xterm-color" APP_HOME="/srv" APP_OPT="/opt/app"  
ENV APP_FILES="${APP_HOME}/files" APP_BACKUPS="${APP_HOME}/backups"
APP_LOGS="${APP_HOME}/logs" APP_CONF="${APP_HOME}/conf"  
# define local variables first (to easy maintain in future)  
RUN export S6_OVERLAY_VER=1.17.2.0 && \  
# fixed alpine bug when /etc/hosts isn't processed  
echo 'hosts: files dns' >> /etc/nsswitch.conf && \  
# install ca certs to communicate external sites by SSL  
# and rsync as we'ar using it to syncronize folders  
# and bush as a lot of customers like it  
apk add \--update libressl ca-certificates rsync bash curl wget nmap-ncat
busybox-suid less grep sed tar gzip nano && \  
# install s6-overlay (https://github.com/just-containers/s6-overlay)  
wget -qO- https://s3.amazonaws.com/wodby-
releases/s6-overlay/v${S6_OVERLAY_VER}/s6-overlay-amd64.tar.gz | tar xz -C /
&& \  
# clear cache data and disable su  
rm -rf /var/cache/apk/* /tmp/* /usr/bin/su  
  
# default entrypoint, never overright it  
ENTRYPOINT ["/init"]

