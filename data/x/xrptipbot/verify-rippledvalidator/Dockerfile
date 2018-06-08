FROM certbot/certbot:latest  
  
MAINTAINER Wietse Wind <mail@wietse.com>  
  
ENTRYPOINT [ "/entrypoint" ]  
EXPOSE 80  
WORKDIR /  
  
RUN apk update && \  
apk add openssl curl && \  
pip install pystun && \  
rm -rf /var/cache/apk/*  
  
COPY entrypoint /entrypoint

