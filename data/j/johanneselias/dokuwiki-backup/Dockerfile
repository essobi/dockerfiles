FROM johanneselias/ubuntu1704-apache2-php-perl:1.0  
RUN apt-get -y update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
php-sqlite3 \  
postfix  
  
WORKDIR /setup  
RUN wget http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz; \  
tar xvf dokuwiki-stable.tgz; \  
mv dokuwiki-*/ dokuwiki  
  
COPY helper/dokuwiki-* /usr/bin/  
  
RUN chmod 700 /usr/bin/dokuwiki-*  
  
ENTRYPOINT ["dokuwiki-configure"]  
  

