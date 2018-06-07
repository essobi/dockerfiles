FROM webhippie/alpine:latest  
MAINTAINER Thomas Boerger <thomas@webhippie.de>  
  
VOLUME ["/srv/app"]  
  
WORKDIR /srv/app  
ENTRYPOINT ["/usr/bin/hugo"]  
CMD ["server"]  
  
RUN apk update && \  
apk add \  
make \  
git \  
hugo && \  
rm -rf \  
/var/cache/apk/*  

