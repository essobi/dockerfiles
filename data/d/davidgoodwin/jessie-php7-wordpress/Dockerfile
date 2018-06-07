FROM debian:jessie-slim  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
COPY dotdeb.key.gpg /etc/apt/trusted.gpg.d/dotdeb.gpg  
COPY dotdeb.list /etc/apt/sources.list.d/dotdeb.list  
COPY apache-site.conf /etc/apache2/sites-available/default.conf  
COPY php-local.ini /etc/php/7.0/apache2/conf.d/php-local.ini  
COPY msmtprc /etc/msmtprc  
  
#RUN /bin/ip addr list && cat /etc/resolv.conf && ip route list  
RUN apt-get update && \  
apt-get install -y ca-certificates curl php7.0 libapache2-mod-php7.0
php7.0-xsl php7.0-xml php7.0-zip php7.0-gd php7.0-pdo php7.0-opcache
php7.0-mysql php7.0-curl php7.0-cli php7.0-intl msmtp-mta && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
COPY apache-security.conf /etc/apache2/conf-available/security.conf  
  
RUN /usr/sbin/a2enmod rewrite deflate expires headers php7.0 && \  
echo GMT > /etc/timezone && dpkg-reconfigure --frontend noninteractive tzdata
&& \  
ln -sf /dev/stdout /var/log/apache2/access.log && ln -sf /dev/stderr
/var/log/apache2/error.log  
  
WORKDIR /var/www/htdocs  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
  
EXPOSE 80  

