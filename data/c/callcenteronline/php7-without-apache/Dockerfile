FROM ubuntu:trusty  
  
  
  
RUN apt-get update && apt-get install -y apt-utils net-tools inetutils-ping
sudo  
RUN sudo apt-get install -y python-software-properties software-properties-
common python3-software-properties  
  
RUN sudo apt-get autoremove --purge php5-*  
RUN sudo apt-get install -y language-pack-en-base  
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php -y  
RUN sudo apt-get update  
RUN sudo apt-get install -y php7.0 php7.0-cgi php7.0-cli php7.0-curl
php7.0-imap php7.0-ldap php7.0-pgsql php7.0-mcrypt php7.0-sqlite3 php7.0-mysql
php7.0-json php7.0-fpm php7.0-xmlrpc php7.0-gd php7.0-common php7.0-odbc
php7.0-opcache php7.0-readline php7.0-intl php7.0-phpdbg php7.0-tidy
php7.0-mbstring php7.0-xml php7.0-zip php7.0-ssh2 mcrypt libmcrypt-dev  
  
RUN sudo apt-get install mariadb-client -y  
RUN sudo apt-get install mc -y  
  
CMD bash  

