FROM supermp/php  
MAINTAINER supermp <supermp@foxmail.com>  
  
ENV MANTISBT_VERSION 2.2.2  
  
RUN curl -L -o mantisbt.tar.gz
https://github.com/mantisbt/mantisbt/archive/release-${MANTISBT_VERSION}.tar.gz
\  
&& tar xzf mantisbt.tar.gz \  
&& rm -f mantisbt.tar.gz \  
&& chown -R www-data:www-data .  

