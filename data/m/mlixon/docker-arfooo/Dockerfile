FROM mlixon/docker-apache2-php  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
zip && \  
rm -rf /var/lib/apt/lists/*  
  
USER 1000  
RUN mkdir -p /var/www/html  
  
RUN curl -L http://www.e-dir.fr/arfooo_ultimate/arfooo_ultimate.zip >
/var/www/html/arfooo_ultimate.zip && \  
unzip /var/www/html/arfooo_ultimate.zip -d /var/www/html/ && \  
mv /var/www/html/arfooo\ ultimate/* /var/www/html/ && \  
rm /var/www/html/arfooo_ultimate.zip && \  
rm -rf /var/www/html/arfooo\ ultimate/* && \  
rm -rf /var/www/html/arfooo\ ultimate/  
  
RUN echo "Options +FollowSymlinks \n\  
RewriteEngine On \n\  
RewriteBase / \n\  
RewriteCond %{REQUEST_FILENAME} !-f \n\  
RewriteCond %{REQUEST_FILENAME} !-d \n\  
RewriteRule ^(.+)$ index.php" > /var/www/html/.htaccess  
  
USER root  

