FROM gliderlabs/alpine:3.3  
MAINTAINER Dan Sloan <dan@dansloan.org>  
  
ENV ETCD_SRV_DOMAIN="example.com" \  
ETCD_SRV_RECORD="_etcd-server-ssl._tcp.example.com"  
# Update package index when we install nginx  
# TODO: Replace once we have a confd package to install:  
#RUN apk add --update s6 confd  
RUN apk add --update s6  
  
# Copy over our bootup routines.  
# These get config from etcd, and launches any services in the container  
COPY docker-init /docker-init  
  
# This is a thorn in my side. There is no good way to get certificate+key
files  
# delivered into the container on create. Hence, we do it this way.  
VOLUME ["/docker-init/ssl"]  
  
# init.sh copies the s6 services to a temporary location and starts s6-svscan  
# The copying is not strictly necessary (we could launch s6-svscan directly),  
# but I like this approach better, and the paths are shorter (/s6/<service>).  
ENTRYPOINT ["/docker-init/init.sh"]  
  
# CMD is not required.  

