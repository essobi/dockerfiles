FROM gentux/php-laravel:latest  
RUN apt-get update  
RUN apt-get install -y wget  
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ jessie-pgdg main' >>
/etc/apt/sources.list.d/postgresql.list  
RUN wget --no-check-certificate -q
https://www.postgresql.org/media/keys/ACCC4CF8.asc -O- | apt-key add -  
RUN apt-get update  
RUN apt-get install -y postgresql-client-9.6  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
RUN mv composer.phar /usr/local/bin/composer  
RUN wget
https://github.com/generationtux/par/releases/download/v0.0.2/par_linux_amd64  
RUN mv par_linux_amd64 par  
RUN chmod +x ./par  
RUN mv ./par /usr/local/bin/  

