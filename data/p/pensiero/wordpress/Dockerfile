FROM pensiero/apache-php-mysql  
  
# Labels  
LABEL maintainer "oscar.fanelli@gmail.com"  
# Mysql packages  
RUN apt update -q && apt install -yqq --force-yes \  
php-cli \  
php-gd \  
php-imagick \  
php-mcrypt \  
php-xml \  
php-xmlrpc \  
php-zip  
  
# Postfix  
# Note: we disable IPv6 for now, IPv6 is available in Docker even if the host
does not have IPv6 connectivity  
RUN apt-get update -q -q && \  
echo postfix postfix/main_mailer_type string "'Internet Site'" | debconf-set-
selections && \  
echo postfix postfix/mynetworks string "127.0.0.0/8" | debconf-set-selections
&& \  
echo postfix postfix/mailname string temporary.example.com | debconf-set-
selections && \  
apt-get --yes \--force-yes install postfix && \  
postconf -e mydestination="localhost.localdomain, localhost" && \  
postconf -e smtpd_banner='$myhostname ESMTP $mail_name' && \  
postconf -# myhostname && \  
postconf -e inet_protocols=ipv4 && \  
apt-get --yes \--force-yes \--no-install-recommends install rsyslog && \  
sed -i 's/\/var\/log\/mail/\/var\/log\/postfix\/mail/'
/etc/rsyslog.d/50-default.conf  
  
# Start services  
COPY ./start.sh /root/start.sh  
CMD ["/root/start.sh"]

