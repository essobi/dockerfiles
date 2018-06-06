FROM busybox:buildroot-2014.02  
MAINTAINER Pascha Butretell <admin@pascha.domains>  
  
RUN adduser -u 3342 -D pascha \  
&& mkdir -p /volumes/certs-data \  
&& chown pascha:pascha /volumes/certs-data \  
&& chmod 770 /volumes/certs-data  
  
VOLUME ["/volumes/certs-data"]

