FROM alpine:3.5  
MAINTAINER Erwan SEITE <wanix(dot)fr(at)gmail(dot)com>  
  
RUN mkdir -p /srv/inkscape  
RUN apk add --update --no-cache inkscape fontconfig ttf-dejavu  
  
WORKDIR /srv/inkscape  
VOLUME ["/srv/inkscape"]  
  
CMD ["inkscape", "--help"]  

