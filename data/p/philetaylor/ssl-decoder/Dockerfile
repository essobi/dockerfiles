FROM million12/nginx-php:php70  
  
MAINTAINER Phil Taylor <phil@phil-taylor.com>  
  
RUN rm -Rf /data/www/default \  
&& curl
https://gist.githubusercontent.com/PhilETaylor/d23c36c374d5784a1fd55f58259f3276/raw/afc21dbaa9fda48bfe35725f76c4e22569cf418b/gistfile1.txt
> /etc/nginx/hosts.d/ssldecoder.conf \  
&& mkdir -p /code \  
&& git clone https://github.com/PhilETaylor/ssl-decoder.git /code \  
&& chown -Rf www:www /code  
  
EXPOSE 80

