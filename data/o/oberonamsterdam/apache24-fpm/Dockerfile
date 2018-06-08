FROM httpd:2.4  
MAINTAINER chin@oberon.nl  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN mkdir -p /app && \  
mkdir -p /usr/local/apache2/conf/other/  
  
RUN apt update && apt install -y libapache2-mod-auth-openidc && rm -rf
/var/lib/apt/lists/*  
  
COPY app.conf /usr/local/apache2/conf/other/app.conf  
COPY production.conf /usr/local/apache2/conf/other/production.conf  
COPY php-fpm.conf /usr/local/apache2/conf/other/php-fpm.conf  
RUN echo 'IncludeOptional /usr/local/apache2/conf/other/*.conf' >>
/usr/local/apache2/conf/httpd.conf  
  
# ENV  
VOLUME /app  
WORKDIR /app  
ENV TERM xterm  
ENV APACHE_DOCUMENTROOT /app  

