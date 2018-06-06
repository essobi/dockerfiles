FROM busybox:buildroot-2014.02  
MAINTAINER Pascha Butretell <admin@pascha.domains>  
  
RUN adduser -u 3342 -D pascha \  
&& mkdir -p /volumes/consul-conf \  
&& chown pascha:pascha /volumes/consul-conf \  
&& chmod 770 /volumes/consul-conf  
  
VOLUME ["/volumes/consul-conf"]

