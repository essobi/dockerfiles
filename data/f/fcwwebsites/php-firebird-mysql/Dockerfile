FROM ubuntu:14.04.4  
MAINTAINER Feijao Costa <feijao@feijaocosta.com.br>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# Install nginx, php5, php interbase/firebird module and supervisor  
RUN \  
apt-get update && \  
apt-get install -y nginx-light && \  
apt-get install -y php5-fpm && \  
sed -ri 's/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g' /etc/php5/fpm/php.ini &&
\  
apt-get install -y php5-interbase && \  
apt-get install -y php5-gd php5-mysql && \  
php5enmod interbase && \  
apt-get install -y supervisor && \  
mkdir -p /etc/supervisor/conf.d/ && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY ./build/nginx/default /etc/nginx/sites-available/default  
COPY ./build/supervisor/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
  
VOLUME /usr/share/nginx/html  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]  

