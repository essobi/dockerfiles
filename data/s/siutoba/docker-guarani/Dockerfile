FROM siutoba/docker-web:latest  
MAINTAINER ablanco@siu.edu.ar  
  
COPY gestion.sh /entrypoint.d/  
COPY autogestion.sh /entrypoint.d/  
RUN mkdir /var/local/autogestion_conf/  
COPY var/autogestion/* /var/local/autogestion_conf/  
  
ENV JASPER_HOST jasper  
ENV JASPER_PORT 8081  
RUN apt-get update -qq && apt-get install -y libpq-dev && docker-php-ext-
install pgsql && apt-get remove -y libpq-dev  
RUN chmod +x /entrypoint.d/*.sh  
  

