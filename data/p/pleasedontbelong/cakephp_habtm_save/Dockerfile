FROM linode/lamp  
RUN apt-get update && apt-get install -y php5-mysql && a2enmod rewrite  
  
RUN mkdir /code  
WORKDIR /code  
ADD . /code/  
  
COPY main_website.conf /etc/apache2/sites-available/  
RUN rm /etc/apache2/sites-enabled/example.com.conf && \  
ln -s /etc/apache2/sites-available/main_website.conf /etc/apache2/sites-
enabled/main_website.conf && \  
mkdir /var/log/main_website/  
  
RUN service mysql start && \  
mysql -u root -pAdmin2015 --execute="CREATE DATABASE cake_habtm; GRANT ALL ON
cake_habtm.* TO 'cake_user' IDENTIFIED BY 'cake_pwd'; FLUSH PRIVILEGES;" && \  
mysql -u cake_user -pcake_pwd cake_habtm < /code/database/cake-habtm.sql  
  
RUN mkdir /tmp/cake_habtm && cp -R app/tmp/* /tmp/cake_habtm && chown -R www-
data:www-data /tmp/cake_habtm  
  
EXPOSE 80  
ENTRYPOINT ["/code/services.sh"]  

