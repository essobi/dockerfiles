FROM debian:jessie  
MAINTAINER Salvatore Caputi <salvatore@scaputi.net>  
  
RUN apt-get update && apt-get install -y \  
nano \  
apache2 \  
php5 \  
php5-common \  
php5-cli \  
php5-mysql \  
php5-curl \  
wget \  
git \  
ruby  
RUN gem install sass  
  
ENV TERM xterm  
  
COPY aliases /tmp/aliases  
RUN cat /tmp/aliases >> /root/.bashrc  
  
RUN a2enmod rewrite  
RUN a2enmod alias  
  
COPY apache-start.sh /usr/local/bin/apache-start  
RUN chmod +x /usr/local/bin/apache-start  
  
COPY install-composer.sh /usr/local/bin/install-composer  
RUN chmod +x /usr/local/bin/install-composer  
RUN ["install-composer"]  
  
CMD ["apache-start"]  
  
EXPOSE 80  

