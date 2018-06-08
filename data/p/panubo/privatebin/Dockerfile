FROM docker.io/panubo/php-apache:debian8  
  
MAINTAINER Andrew Cutler <andrew@panubo.io>  
  
ENV PRIVATEBIN_VERSION=1.1.1
PRIVATEBIN_SRC=https://github.com/PrivateBin/PrivateBin.git  
  
RUN cd /var/www/html/ \  
&& git clone $PRIVATEBIN_SRC . \  
&& [ "$PRIVATEBIN_VERSION" != 'master' ] && git checkout
tags/$PRIVATEBIN_VERSION || git checkout master \  
&& rm -rf .git \  
&& mv .htaccess.disabled .htaccess \  
;  
  
COPY conf.php /var/www/html/cfg/  
COPY Mountfile /var/www/html/  

