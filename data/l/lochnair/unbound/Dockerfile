FROM lochnair/base:alpine  
MAINTAINER Nils Andreas Svee <me@lochnair.net>  
  
LABEL Description="Unbound image based on Alpine Linux"  
  
RUN apk add \  
\--no-cache \  
\--update \  
unbound  
  
COPY root/ /  
  
RUN rm -v /etc/unbound/*  
  
VOLUME /etc/unbound

