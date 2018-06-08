FROM php:apache  
LABEL maintainer="https://github.com/h3po"  
  
ARG VERSION=0.14.0  
ADD https://github.com/MoonchildProductions/FSyncMS/archive/${VERSION}.tar.gz
/tmp  
  
RUN \  
docker-php-ext-install pdo pdo_mysql && \  
tar xf /tmp/*.tar.gz -C /tmp && \  
rm /tmp/*.tar.gz && \  
mv /tmp/FSyncMS-${VERSION}/*.php /var/www/html/  
  
ENV DBTYPE=sqlite  
ENV DBHOST=db  
ENV DBNAME=fsyncms  
ENV DBUSER=fsyncms  
ENV DBPASS=snakeoil  
ENV ENABLE_REGISTER=true  
  
VOLUME /var/www/html  
  
COPY setup.sh /  
  
ENTRYPOINT ["/bin/bash"]  
CMD ["-c", "/setup.sh && docker-php-entrypoint apache2-foreground"]  

