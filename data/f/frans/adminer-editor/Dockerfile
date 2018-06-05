FROM adminer  
MAINTAINER Frans Kunst frans@atux.nl  
RUN \  
cd /var/www/html && \  
curl -L
https://github.com/vrana/adminer/releases/download/v4.3.1/editor-4.3.1-mysql.php
-o editor.php  
COPY adminer-editor.php /var/www/html/  
EXPOSE 8080  

