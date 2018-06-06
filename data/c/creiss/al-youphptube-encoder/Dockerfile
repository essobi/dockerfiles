# Parent Image  
FROM ubuntu:latest  
  
# Set some Meta-Info  
LABEL maintainer="Christian Reiss (email@christian-reiss.de)"  
LABEL net.alpha-labs.version="0.1"  
LABEL vendor="alpha-labs.net"  
LABEL net.alpha-labs.release-date="2017-11-19"  
LABEL net.alpha-labs.version.is-production="true"  
  
# Install required packages & System Update  
RUN apt update && apt upgrade -y && DEBIAN_FRONTEND=noninteractive apt install
-y apache2 monit php7.0 libapache2-mod-php7.0 php7.0-mysql php7.0-curl
php7.0-gd php7.0-intl mysql-client ffmpeg git libimage-exiftool-perl python
curl  
  
# Clone the Repo & Download youtube-dl  
RUN cd /var/www/ && rm -rf html && git clone
https://github.com/DanielnetoDotCom/YouPHPTube-Encoder.git && mv YouPHPTube-
Encoder html  
RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o
/usr/local/bin/youtube-dl && chmod a+rx /usr/local/bin/youtube-dl  
RUN mkdir /var/www/html/videos && chown www-data:www-data /var/www/html/videos  
  
# Install Monit  
COPY monitrc /etc/monitrc  
RUN /bin/chmod 0700 /etc/monitrc  
  
# Data Exchange  
VOLUME /var/www/html/videos  
EXPOSE 80/tcp  
  
# youphptube config  
RUN a2enmod rewrite  
COPY apache.conf /etc/apache2/conf-enabled/youphptube.conf  
COPY php.ini /etc/php/7.0/apache2/conf.d/youphptube.ini  
  
# Run it.  
ENTRYPOINT /usr/bin/monit -c /etc/monitrc -I  
  

