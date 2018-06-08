FROM php:7.0-apache  
MAINTAINER MOKHTARI Alexis <dev.mokhtaria@gmail.com>  
  
RUN apt-get update -y  
  
ENV TZ=Europe/Paris  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
ENV DOKU_VER 2017-02-19b  
  
RUN cd /var/www && \  
curl -O -L "https://download.dokuwiki.org/src/dokuwiki/dokuwiki-$DOKU_VER.tgz"
&& \  
tar -xzf dokuwiki-$DOKU_VER.tgz && \  
mkdir /var/www/doku && \  
mkdir /var/www/doku/lib && \  
mv /var/www/dokuwiki-$DOKU_VER/lib/plugins /var/www/doku/lib/ && \  
mv /var/www/dokuwiki-$DOKU_VER/data /var/www/doku/ && \  
mv /var/www/dokuwiki-$DOKU_VER/conf /var/www/doku/ && \  
mv /var/www/dokuwiki-$DOKU_VER/lib/tpl /var/www/doku/lib/  
  
ADD ./security.conf /etc/apache2/conf-available/security.conf  
  
ADD ./start.sh /usr/local/bin/start  
  
RUN start  
  
ADD ./dir_chmod.sh /usr/local/bin/htmlchmod  
  

