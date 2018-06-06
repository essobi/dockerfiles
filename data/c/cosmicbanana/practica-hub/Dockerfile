FROM debian:jessie  
RUN apt-get update && apt-get install -y apache2 php5 libapache2-mod-php5 &&
apt-get clean && rm -rf /var/lib/apt/lists/*  
RUN ln -sf /proc/self/fd/1 /var/log/apache2/access.log && ln -sf
/proc/self/fd/1 /var/log/apache2/error.log  
COPY info.php /var/www/html  
ENTRYPOINT ["/usr/sbin/apachectl", "-D", "FOREGROUND"]  
  

