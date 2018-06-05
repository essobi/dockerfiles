FROM istepanov/dokuwiki  
  
RUN apt-get update && apt-get install -y \  
apt-utils \  
curl libcurl3 libcurl3-dev php5-curl php5-mcrypt && php5enmod curl && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /var/dokuwiki-storage/  
  
# append a line to start.sh  
# run as www-data: "php bin/indexer.php -c"  
RUN sed -i '7 a su -s /bin/bash www-data -c "'"php /var/www/bin/indexer.php
-c"'"' /start.sh && \  
rm -rf /var/www/lib/plugins/ && \  
ln -s /var/dokuwiki-storage/lib/plugins /var/www/lib/plugins && \  
rm -rf /var/www/lib/styles/ && \  
ln -s /var/dokuwiki-storage/lib/styles /var/www/lib/styles && \  
rm -rf /var/www/lib/tpl/ && \  
ln -s /var/dokuwiki-storage/lib/tpl /var/www/lib/tpl  

