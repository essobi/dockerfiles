FROM nginx:latest  
  
# Dockerfile author / maintainer  
MAINTAINER Jon Klixbüll Langeland <jolj@dr.dk>  
  
LABEL Description="This docker container provides Nginx binaries and
configuration"  
LABEL Vendor="Danish Broadcasting Corporation"  
LABEL Version="2.0.0"  
LABEL Team="Team Web API" \  
Team.mail="dl-TeamWebAPI@dr.dk"  
  
RUN mkdir /etc/nginx/conf.temp  
RUN mkdir /etc/nginx/sites-enabled  
  
#RUN echo "upstream php-upstream { server php-fpm:9000; }" >
/etc/nginx/conf.d/upstream.conf  
RUN usermod -u 1000 www-data  
  
COPY default.tmpl.conf /etc/nginx/conf.temp/default.tmpl.conf  
COPY run.sh /bin/run.sh  
  
ENV NGINX_PATH_PREFIX "tjenester/application"  
ENV NGINX_WEBROOT "/var/www/application/web"  
ENV NGINX_DOMAIN dev.dr.dk  
ENV NGINX_CERTIFICATE_URL ""  
ENV NGINX_PHP_HOST_AND_PORT php:9000  
ENV NGINX_TRY_FILES $$uri /app.php$$is_args$$args  
  
RUN apt-get -qq update \  
&& apt-get install -y \  
curl \  
openssl \  
\--no-install-recommends  
  
RUN mkdir /etc/nginx/ssl/  
  
WORKDIR /var/www/application  
CMD /bin/run.sh  

