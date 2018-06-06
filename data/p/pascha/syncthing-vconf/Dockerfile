FROM busybox:buildroot-2014.02  
MAINTAINER Pascha Butretell <admin@pascha.domains>  
  
RUN adduser -u 3342 -D pascha \  
&& mkdir -p /volumes/syncthing-conf \  
&& chown pascha:pascha /volumes/syncthing-conf \  
&& chmod 770 /volumes/syncthing-conf  
  
VOLUME ["/volumes/syncthing-conf"]

