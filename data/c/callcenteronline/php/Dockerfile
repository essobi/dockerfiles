FROM callcenteronline/apache  
  
RUN apt-get install php7.0 libapache2-mod-php7.0 -y && apt-get install php-
curl -y  
RUN apt-get install php-zip -y  
RUN apt-get install php-xml -y  
RUN apt-get install php7.0-cli php7.0-fpm php7.0-json php7.0-readline -y  
RUN apt-get install php-mysqlnd -y  
RUN apt-get install git -y  
RUN apt-get install composer -y  
RUN apt-get install mariadb-client -y  
RUN apt-get install php-ssh2 -y  
RUN apt-get install vim -y  
  
WORKDIR /var/www/html/  
CMD service apache2 start && bash  

