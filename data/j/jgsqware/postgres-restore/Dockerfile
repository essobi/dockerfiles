FROM alpine  
MAINTAINER Julien Garcia Gonzalez <jgonzalez@wemanity.com>  
  
RUN apk add --update \  
postgresql \  
  
&& rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/pg_restore"]  

