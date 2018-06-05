FROM laraedit/laraedit  
  
######################################################  
##Adding auth to bitbucket's repository  
######################################################  
RUN mkdir /root/.ssh  
COPY build/id_rsa /root/.ssh/bitbucket_rsa  
COPY build/id_rsa.pub /root/.ssh/bitbucket_rsa.pub  
COPY build/config /root/.ssh/config  
RUN cd /root/.ssh/ && chmod 400 bitbucket_rsa  
  
RUN apt-get update  
RUN apt-get install -y --force-yes php7.0-ldap php7.0-soap php7.0-sybase
freetds-common libsybdb5  
  
######################################################  
##Cloning the repo  
######################################################  
RUN git clone git@bitbucket.org:uaicloudlab/rfc.git /var/www/html/rfc  
# RUN cd /var/www/html/rfc/  
COPY build/.env /var/www/html/rfc/  
######################################################  
#Folder Permissons and Nginx Conf  
######################################################  
  
RUN sed -i 's,root /var/www/html/app/public,root /var/www/html/rfc/public,g'
/etc/nginx/sites-available/homestead  
RUN chown -R www-data.www-data /var/www/html/rfc  
RUN chown -R www-data.www-data /var/www/html/  
RUN chmod -R 755 /var/www/html/rfc  
RUN chmod -R 777 /var/www/html/rfc/storage  
  
######################################################  
#Enable Loggin  
######################################################  
RUN sed -i 's,;php_admin_value[error_log] = /var/log/fpm-
php.www.log,php_admin_value[error_log] = /var/log/fpm-php.www.log,g'
/etc/php/7.0/fpm/pool.d/www.conf  
RUN sed -i 's,;php_admin_flag[log_errors] = on,php_admin_flag[log_errors] =
on,g' /etc/php/7.0/fpm/pool.d/www.conf  
  
  
######################################################  
#Change Max  
######################################################  
RUN sed -i 's,; max_input_vars = 1000, max_input_vars = 9999999,g'
/etc/php/7.0/fpm/php.ini  
  
COPY build/Laravelqueue.conf /etc/supervisor/conf.d/Laravelqueue.conf  
  
######################################################  
#Configure LDAP, SOAP and MSSQL  
######################################################  
#RUN sed -i 's,extension=php_ldap.dll,;extension=php_ldap.dll,g'
/etc/php/7.0/cli/php.ini  
#RUN sed -i 's,extension=php_pdo_mysql.dll,;extension=php_pdo_mysql.dll,g'
/etc/php/7.0/cli/php.ini  
#RUN sed -i
's,extension=extension=php_soap.dll,;extension=extension=php_soap.dll,g'
/etc/php/7.0/cli/php.ini  
######################################################  
#Install App  
######################################################  
RUN cd /var/www/html/rfc && composer install --no-scripts  
RUN cd /var/www/html/rfc && bower install --allow-root  
RUN cd /var/www/html/rfc && npm install  
  
RUN rm /var/www/html/rfc/.env  
COPY build/production_env /var/www/html/rfc/.env  
COPY build/run.sh /opt/run.sh  
RUN dos2unix /opt/run.sh  
RUN chmod u+x /opt/run.sh  
######################################################  
#Restart Services  
######################################################  
#RUN service nginx stop  
#RUN service nginx start  
  
VOLUME ["/var/www/html/rfc"]  
  
#exposing port for socket.io  
EXPOSE 3000  
######################################################  
#SET LOGIN HOME  
######################################################  
  
ENV HOME /var/www/html/rfc  
  
# Restart Services and Folder Permissions  
RUN service php7.0-fpm restart  
#ENTRYPOINT ["/opt/run.sh"]  

