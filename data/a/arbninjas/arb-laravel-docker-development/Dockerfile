#  
#--------------------------------------------------------------------------  
# Image Setup  
#--------------------------------------------------------------------------  
#  
FROM phusion/baseimage:latest  
  
MAINTAINER Melchor O. Abcede Jr <melchor.abcede@loannotify.com>  
  
RUN DEBIAN_FRONTEND=noninteractive  
RUN locale-gen en_US.UTF-8  
  
ENV LANGUAGE=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8  
ENV LC_CTYPE=UTF-8  
ENV LANG=en_US.UTF-8  
ENV TERM xterm  
  
# Add the "PHP 7.1" ppa  
RUN apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:ondrej/php  
  
#For running web controllers/api in browser  
RUN apt-get update  
RUN apt-get -y install freetds-common freetds-bin unixodbc php7.1-sybase  
  
#  
#--------------------------------------------------------------------------  
# Software's Installation  
#--------------------------------------------------------------------------  
#  
# Install "PHP Extentions", "libraries", "Software's"  
RUN apt-get update && \  
apt-get install -y php7.1 mcrypt php7.1-mcrypt php-mbstring php-pear
php7.1-dev php7.1-xml \  
git \  
curl \  
vim \  
nano \  
&& apt-get clean  
  
#####################################  
# Composer:  
#####################################  
# Install composer and add its bin to the PATH.  
RUN curl -s http://getcomposer.org/installer | php && \  
echo "export PATH=${PATH}:/var/www/vendor/bin" >> ~/.bashrc && \  
mv composer.phar /usr/local/bin/composer  
  
# Source the bash  
RUN . ~/.bashrc  
  
RUN apt-get install screen  
  
# Check if NVM needs to be installed  
ARG NODE_VERSION=stable  
ENV NODE_VERSION ${NODE_VERSION}  
ARG INSTALL_NODE=true  
ENV INSTALL_NODE ${INSTALL_NODE}  
ENV NVM_DIR /home/laradock/.nvm  
RUN if [ ${INSTALL_NODE} = true ]; then \  
# Install nvm (A Node Version Manager)  
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.6/install.sh |
bash && \  
. $NVM_DIR/nvm.sh && \  
nvm install ${NODE_VERSION} && \  
nvm use ${NODE_VERSION} && \  
nvm alias ${NODE_VERSION} && \  
npm install -g gulp bower vue-cli \  
;fi  
  
# Wouldn't execute when added to the RUN statement in the above block  
# Source NVM when loading bash since ~/.profile isn't loaded on non-login
shell  
RUN if [ ${INSTALL_NODE} = true ]; then \  
echo "" >> ~/.bashrc && \  
echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.bashrc && \  
echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm' >>
~/.bashrc \  
;fi  
  
# Add NVM binaries to root's .bashrc  
USER root  
  
RUN if [ ${INSTALL_NODE} = true ]; then \  
echo "" >> ~/.bashrc && \  
echo 'export NVM_DIR="/home/laradock/.nvm"' >> ~/.bashrc && \  
echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" # This loads nvm' >>
~/.bashrc \  
;fi  
  
########################  
#MYSQL  
########################  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
  
# MySQL Server  
RUN echo 'mysql-server mysql-server/root_password password root' | debconf-
set-selections  
RUN echo 'mysql-server mysql-server/root_password_again password root' |
debconf-set-selections  
RUN apt-get -y install mysql-server --no-install-recommends  
RUN sed -ie "s/^bind-address\s*=\s*127\\.0\\.0\\.1$/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
#########################  
#Install PhpmyAdmin  
#########################  
#Add a comment to this line  
ENV APP_PASS="root"  
ENV ROOT_PASS="root"  
ENV APP_DB_PASS="root"  
RUN echo "phpmyadmin phpmyadmin/dbconfig-install boolean true" | debconf-set-
selections  
RUN echo "phpmyadmin phpmyadmin/app-password-confirm password $APP_PASS" |
debconf-set-selections  
RUN echo "phpmyadmin phpmyadmin/mysql/admin-pass password $ROOT_PASS" |
debconf-set-selections  
RUN echo "phpmyadmin phpmyadmin/mysql/app-pass password $APP_DB_PASS" |
debconf-set-selections  
RUN echo "phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2" |
debconf-set-selections  
#RUN echo "phpmyadmin phpmyadmin/remote/port 3306"  
RUN apt-get install -y phpmyadmin  
  
RUN service apache2 start  
  
####################################  
#Install ms sql server-tools  
####################################  
ENV ACCEPT_EULA=Y  
  
  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list | tee
/etc/apt/sources.list.d/msprod.list  
RUN apt-get update  
RUN apt-get install -y msodbcsql mssql-tools  
RUN apt-get install -y unixodbc-dev  
  
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile  
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc  
RUN echo 'source ~/.bashrc'  
  
RUN pear config-set php_ini `php --ini | grep "Loaded Configuration" | sed -e
"s|.*:\s*||"` system  
RUN pecl install sqlsrv  
RUN pecl install pdo_sqlsrv  
RUN pecl install sqlsrv-4.1.7preview  
RUN pecl install pdo_sqlsrv-4.1.7preview  
  
RUN service apache2 restart  
  
#Setup App's PORT  
ENV APPPORT=3000  
COPY laravel.conf /etc/apache2/sites-available/laravel.conf  
  
#This will only work with GNU sed  
RUN sed -i.bak "s/Listen 80/Listen 80\n\nListen $APPPORT\n/"
/etc/apache2/ports.conf  
  
RUN a2ensite 000-default && \  
a2ensite laravel.conf && \  
a2enmod rewrite  
  
RUN echo 'mkdir /var/www/application'  
  
EXPOSE 3000  
EXPOSE 80  

