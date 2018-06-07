############################################################  
# Dockerfile to build wEMBOSS container image for the eBioKit  
# Based on ubuntu:16.04  
# Version 0.1 August 2017  
# TODO LIST:  
# - Use alpine linux to reduce image size  
# - Sign up form  
############################################################  
  
# Set the base image to official ubuntu:16.04  
FROM ubuntu:16.04  
  
# File Author / Maintainer  
MAINTAINER Rafael Hernandez <https://github.com/fikipollo>  
  
################## BEGIN INSTALLATION ######################  
#Install dependencies  
RUN apt-get update \  
&& apt-get install -y apache2 curl build-essential emboss ghostscript
apache2-suexec-custom libcgi-pm-perl libmailtools-perl \  
&& a2enmod suexec \  
&& a2enmod cgi \  
&& apt-get clean  
  
#Copy files  
COPY configs/* /tmp/  
  
#Install wEMBOSS and admin tools  
RUN curl -L
https://ayera.dl.sourceforge.net/project/wemboss/wEMBOSS/2.2.1/wEMBOSSDIST-2.2.1.tar.gz
| \  
tar xzf - --strip-components=1 -C /tmp \  
&& cd /tmp/wEMBOSSinstall/ \  
&& cat /tmp/yourAnswers | perl install.pl \  
&& mv /tmp/wemboss.conf /etc/apache2/sites-enabled/000-default.conf \  
&& mv /tmp/entrypoint.sh /usr/bin/entrypoint.sh \  
&& chmod +x /usr/bin/entrypoint.sh \  
&& mv /tmp/index.html /var/www/html/ \  
&& mv /tmp/catch* /usr/local/wEMBOSS/wEMBOSS_cgi/ \  
&& mv /tmp/admin* /usr/local/wEMBOSS/wEMBOSS_cgi/ \  
&& chmod 700 /usr/local/wEMBOSS/wEMBOSS_cgi/* \  
&& rm -r /tmp/* \  
&& sed -i 's#/var/www#/usr/local/wEMBOSS/wEMBOSS_cgi#g'
/etc/apache2/suexec/www-data \  
&& useradd -m wemboss \  
&& htpasswd -b -c /usr/local/wEMBOSS/.htpasswd admin 123 \  
&& htpasswd -b /usr/local/wEMBOSS/.htpasswd test test \  
&& chown -R wemboss:wemboss /usr/local/wEMBOSS/  
  
##################### INSTALLATION END #####################  
  
EXPOSE 80  
  
ENTRYPOINT ["/usr/bin/entrypoint.sh"]  

