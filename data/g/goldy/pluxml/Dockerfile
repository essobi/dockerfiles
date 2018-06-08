FROM php:7.0-fpm-alpine  
  
RUN apk add --no-cache git py-pip unzip curl  
  
RUN git clone https://github.com/pluxml/PluXml.git --branch=5.5
/var/www/pluxml  
  
RUN pip install pyentrypoint==0.3.3  
  
# Add some themes  
RUN curl
http://ressources.pluxml.org/?telechargement/MDE1MS4wMTguMTkzMDMudGhlbWUtY2xlYW4vcHVibGljL2FyY2hpdmUuemlwfHRoZW1lLWNsZWFufHppcCoyYjhmZTQ,
> /var/www/pluxml/themes/theme-clean.zip && \  
unzip /var/www/pluxml/themes/theme-clean.zip -d /var/www/pluxml/themes/ ||
true ; \  
rm /var/www/pluxml/themes/theme-clean.zip  
  
RUN curl
http://ressources.pluxml.org/?telechargement/MDE1My4wMTguMTkzMDMudGhlbWUtY2xvc2VzdC9wdWJsaWMvYXJjaGl2ZS56aXB8dGhlbWUtY2xvc2VzdHx6aXAqYWU2ODI1
> /var/www/pluxml/themes/theme-closest.zip && \  
unzip /var/www/pluxml/themes/theme-closest.zip -d /var/www/pluxml/themes/ ||
true ; \  
rm /var/www/pluxml/themes/theme-closest.zip  
  
VOLUME ["/var/www/pluxml", "/var/www/pluxml/data", "/etc/nginx/conf.d/"]  
  
ADD nginx.conf.tpl /usr/local/lib/nginx/pluxml.conf.tpl  
  
ADD entrypoint-config.yml .  
ENTRYPOINT ["pyentrypoint"]  

