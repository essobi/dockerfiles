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
##PDF Parser  
#####################################################  
RUN apt-get install -y --force-yes poppler-utils ghostscript  
  
######################################################  
##Language Configuration  
#####################################################  
RUN sudo locale-gen es_ES.UTF-8  
RUN sudo dpkg-reconfigure locales  
  
  
######################################################  
##Clonning the repo  
######################################################  
RUN git clone git@bitbucket.org:acempresarial/informetributario.git
/var/www/html/acEmpresarial  
COPY build/.env /var/www/html/acEmpresarial/  
######################################################  
#Folder Permissons and Nginx Conf  
######################################################  
  
RUN sed -i 's,root /var/www/html/app/public,root
/var/www/html/acEmpresarial/public,g' /etc/nginx/sites-available/homestead  
RUN chown -R www-data.www-data /var/www/html/acEmpresarial  
RUN chown -R www-data.www-data /var/www/html/  
RUN chmod -R 755 /var/www/html/acEmpresarial  
RUN chmod -R 777 /var/www/html/acEmpresarial/storage  
  
######################################################  
#Configure LDAP, SOAP and MSSQL  
######################################################  
  
RUN sed -i 's,;extension=php_ldap.dll,extension=php_ldap.dll,g'
/etc/php/7.0/cli/php.ini  
RUN sed -i 's,;extension=php_pdo_mysql.dll,extension=php_pdo_mysql.dll,g'
/etc/php/7.0/cli/php.ini  
RUN sed -i
's,;extension=extension=php_soap.dll,extension=extension=php_soap.dll,g'
/etc/php/7.0/cli/php.ini  
  
  
######################################################  
#Install App  
######################################################  
RUN cd /var/www/html/acEmpresarial && composer install --no-scripts  
  
RUN cd /var/www/html/acEmpresarial && npm install  
  
RUN rm /var/www/html/acEmpresarial/.env  
COPY build/production_env /var/www/html/acEmpresarial/.env  
  
######################################################  
#Restart Services  
######################################################  
RUN service php7.0-fpm restart  
#RUN service nginx stop  
#RUN service nginx start  
######################################################  
#SET LOGIN HOME  
######################################################  
  
ENV HOME /var/www/html/acEmpresarial

