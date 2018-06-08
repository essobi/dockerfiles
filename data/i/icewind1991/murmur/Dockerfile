FROM alpine:3.6  
MAINTAINER Robin Appelman <robin@icewind.nl>  
  
ARG MUMBLE_VERSION=1.2.19  
ARG BZIP_URL=https://github.com/mumble-
voip/mumble/releases/download/${MUMBLE_VERSION}/murmur-
static_x86-${MUMBLE_VERSION}.tar.bz2  
  
RUN mkdir -pv /data\  
&& adduser -DHs /sbin/nologin mumble \  
&& apk add \--no-cache murmur \  
&& chown -R mumble:mumble /data  
  
EXPOSE 64738 64738/udp  
  
USER mumble  
  
COPY murmur.ini /etc/murmur.tpl  
COPY init.sh /usr/bin/init.sh  
  
CMD ["/usr/bin/init.sh"]  

