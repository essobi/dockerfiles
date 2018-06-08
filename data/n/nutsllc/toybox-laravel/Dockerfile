FROM nutsllc/toybox-php:7.0-apache  
  
ENV LARAVEL_VERSION=5.3.* \  
DOCUMENT_ROOT=/var/www/laravel/public  
  
RUN cd ${HOME} \  
&& composer create-project --prefer-dist "laravel/laravel=${LARAVEL_VERSION}"
${HOME}/laravel \  
&& tar czf laravel.tar.gz laravel/ \  
&& rm -r laravel/ \  
&& apt-get update && apt-get install -y \  
git \  
nodejs \  
npm \  
&& npm cache clean \  
&& npm install n -g \  
&& n stable \  
&& ln -sf /usr/local/bin/node /usr/bin/node \  
&& npm install -g gulp \  
&& apt-get purge -y nodejs npm  
  
COPY docker-entrypoint.sh /entrypoint-laravel.sh  
  
WORKDIR ${DOCUMENT_ROOT}  
ENTRYPOINT ["/entrypoint-php.sh"]  
CMD ["/entrypoint-laravel.sh","apache2-foreground"]  

