FROM alpine:3.3  
MAINTAINER Stewart V. Wright <stewart@vifortech.com>  
  
RUN apk --update add lighttpd && \  
apk add --virtual build-dependencies git && \  
rm -rf /var/www/localhost/htdocs && cd /var/www/localhost/ && \  
git clone --depth=1 https://github.com/jbt/markdown-editor htdocs && \  
rm -rf /var/www/localhost/htdocs/.git && \  
apk del build-dependencies && \  
rm -rf /var/cache/apk/*  
  
CMD ["lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

