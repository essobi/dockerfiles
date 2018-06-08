FROM alpine:latest  
  
MAINTAINER Jakob Runge <sicarius@g4t3.de>  
  
RUN apk update \  
&& apk add git python3-dev \  
&& rm /var/cache/apk/APKINDEX*tar.gz  
  
RUN git clone https://github.com/runjak/nook2016 /srv/nook2016  
  
WORKDIR /srv/nook2016  
EXPOSE 80  
ENTRYPOINT python3 -m http.server 80  

