FROM debian:jessie  
MAINTAINER Justin Kelly <justin@kelly.org.au>  
  
# Usage:  
# docker run -d --name=apache-php -p 8080:80 -p 8443:443 chriswayg/apache-php  
# webroot: /var/www/html/  
# Apache2 config: /etc/apache2/  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install \  
openssl \  
ca-certificates \  
apache2 \  
libapache2-mod-php5 \  
php5 \  
php5-mysql \  
php5-curl \  
php5-imap \  
php5-gd \  
php5-mcrypt \  
php5-json \  
php5-xsl \  
ssmtp && \  
apt-get clean && rm -r /var/lib/apt/lists/*  
  
# Apache + PHP requires preforking Apache for best results & enable Apache SSL  
# forward request and error logs to docker log collector  
RUN a2dismod mpm_event && \  
a2enmod mpm_prefork \  
ssl \  
rewrite && \  
a2ensite default-ssl && \  
ln -sf /dev/stdout /var/log/apache2/access.log && \  
ln -sf /dev/stderr /var/log/apache2/error.log  
  
#Si settings  
ENV SI_AUTH="SI_AUTH"  
ENV DB_HOST="DB_HOST"  
ENV DB_NAME="DB_NAME"  
ENV DB_PASS="DB_PASS"  
ENV DB_PORT="3306"  
ENV DB_USER="DB_USER"  
ENV VIRTUAL_HOST="VIRTUAL_HOST"  
ENV DOMAIN="DOMAIN"  
ENV AWS_REGION="AWS_REGION"  
ENV AWS_ACCESS_KEY_ID="AWS_ACCESS_KEY_ID"  
ENV AWS_SECRET_ACCESS_KEY="AWS_SECRET_ACCESS_KEY"  
ENV SMTP_HOST="SMTP_HOST"  
ENV SMTP_PASS="SMTP_PASS"  
ENV SMTP_USER="SMTP_USER"  
ENV SMTP_PORT="SMTP_POST"  
ENV SMTP_SECURE="SMTP_SECURE"  
# Add config files  
ADD s3 /s3  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
ADD simpleinvoices/ /v  
ADD ssmtp.conf /etc/ssmtp/ssmtp.conf  
RUN mkdir /usr/local/share/ca-certificates/cacert.org  
ADD certs/cacert.pem /etc/ssl/certs/  
ADD certs/root.crt /usr/local/share/ca-certificates/cacert.org  
ADD certs/class3.crt /usr/local/share/ca-certificates/cacert.org  
RUN sed -i -e "s/;openssl.cafile=/openssl.cafile =
\/etc\/ssl\/certs\/cacert.pem/g" /etc/php5/apache2/php.ini && \  
sed -i -e "s/;openssl.capath=/openssl.capath = \/etc\/ssl\/certs\//g"
/etc/php5/apache2/php.ini  
  
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
RUN update-ca-certificates  
#add folders  
ADD simpleinvoices/ /app  
  
RUN chown -Rf www-data:www-data /app/tmp  
  
EXPOSE 80 443  
WORKDIR /var/www/html  
  
CMD ["/run.sh"]  

