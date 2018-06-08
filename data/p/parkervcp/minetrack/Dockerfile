FROM alpine:latest  
  
MAINTAINER Michael Parker, <parkervcp+docker@gmail.com>  
  
RUN apk update \  
&& apk add nodejs git \  
&& mkdir /srv \  
&& git clone https://github.com/Cryptkeeper/Minetrack.git /srv/minetrack \  
&& cd /srv/minetrack \  
&& npm install  
  
WORKDIR /srv/minetrack  
  
CMD ["node", "app.js"]

