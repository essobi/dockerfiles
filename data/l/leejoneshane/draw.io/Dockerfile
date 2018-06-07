FROM httpd:alpine  
  
RUN apk update \  
&& apk add --no-cache git certbot acme-client openssl ca-certificates \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir /source \  
&& cd /source \  
&& git clone https://github.com/jgraph/draw.io.git \  
&& cp -R /source/draw.io/war/* /usr/local/apache2/htdocs \  
&& chown -R www-data:www-data /usr/local/apache2/htdocs \  
&& rm -rf /source  
  
COPY httpd.conf /usr/local/apache2/conf/httpd.conf  
EXPOSE 80 443  
ENTRYPOINT ["httpd-foreground"]  

