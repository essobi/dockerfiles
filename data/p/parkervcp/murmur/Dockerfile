FROM alpine:3.2  
MAINTAINER Michael Parker, <parkervcp+docker@gmail.com>  
  
RUN apk update \  
&& apk add openssl \  
&& mkdir srv \  
&& cd srv/ \  
&& wget https://github.com/mumble-voip/mumble/releases/download/1.2.12/murmur-
static_x86-1.2.12.tar.bz2 \  
&& tar -xjvf murmur-static_x86-1.2.12.tar.bz2 \  
&& mv murmur-static_x86-1.2.12 murmur  
  
WORKDIR /srv/murmur  
  
CMD ["/srv/murmur/murmur.x86", "-fg"]

