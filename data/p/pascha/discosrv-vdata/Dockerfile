FROM busybox:buildroot-2014.02  
MAINTAINER Pascha Butretell <admin@pascha.domains>  
  
RUN adduser -u 3342 -D pascha \  
&& mkdir -p /volumes/discosrv-data \  
&& chown pascha:pascha /volumes/discosrv-data \  
&& chmod 770 /volumes/discosrv-data  
  
VOLUME ["/volumes/discosrv-data"]

