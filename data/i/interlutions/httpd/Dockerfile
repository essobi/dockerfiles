FROM httpd:2.4-alpine  
  
# Install timezone change utils  
RUN apk add --no-cache tzdata  
  
# Tools to change the uid on run  
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories && \  
apk add --no-cache shadow su-exec  
COPY entrypoint-chuid /usr/local/bin  
  
# Install modular httpd.conf  
COPY ./httpd.conf /usr/local/apache2/conf/httpd.conf  
COPY ./ports.conf /usr/local/apache2/conf/ports.conf  
COPY ./mods /usr/local/apache2/conf/mods/  
RUN mkdir /usr/local/apache2/conf/conf/  
RUN mkdir /usr/local/apache2/conf/sites/  
  
ENTRYPOINT ["entrypoint-chuid"]  
CMD ["httpd-foreground"]  

