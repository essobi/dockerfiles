FROM gliderlabs/alpine:3.4  
MAINTAINER Thomas Coats <thomas@metocean.co.nz>  
  
ENV CONSUL_VERSION=0.6.4  
ADD . /install/  
RUN /install/install.sh  
  
CMD ["/sbin/dumb-init-hacked", "/sbin/runsvdir", "-P", "/etc/service"]  

