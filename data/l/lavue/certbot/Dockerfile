FROM lavue/alpine  
#FROM lavue/alpine:0.4.0-3.7  
LABEL description="Certbot for LaVue from Base Alpine image"  
LABEL maintainer="4ngo.ru@gmail.com"  
  
# Add the ENTRYPOINT script  
COPY cert /usr/local/bin/cert  
  
# Add config vars  
COPY cli.ini /.config/letsencrypt.ini  
  
# Install CertBot  
RUN set -xe \  
&& apk add --update --no-cache --virtual .build-dependencies certbot \  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  
  
# Define the entry point that renew certificates without parameters OR create
new.  
CMD ["cert"]  
  
LABEL version="0.2.3-3.7"  

