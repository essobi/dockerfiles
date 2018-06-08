FROM alpine:3.3  
ADD . /root/score  
RUN apk add --update apache2 php-apache2 php-json php-iconv nodejs \  
&& mkdir /run/apache2 \  
&& cd /root/score \  
&& npm install \  
&& echo -e '<Directory "/var/www/localhost/htdocs">\nAllowOverride
All\n</Directory>' > /etc/apache2/conf.d/allowoverride.conf  
ENTRYPOINT ["/root/score/docker-run.sh"]  
EXPOSE 80  

