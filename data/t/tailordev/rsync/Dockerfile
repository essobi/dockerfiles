FROM alpine  
MAINTAINER TailorDev <hello@tailordev.fr>  
  
RUN apk update && \  
apk add rsync openssh-client && \  
rm -r /var/cache/apk/*  
  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/bin/sh", "/entrypoint.sh"]  

