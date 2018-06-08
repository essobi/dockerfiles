FROM alpine:latest  
MAINTAINER Mike Dougherty <github.com/mikedougherty>  
  
RUN apk add --update \  
graphviz \  
ttf-ubuntu-font-family \  
&& apk del --purge \  
&& rm /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/dot"]  

