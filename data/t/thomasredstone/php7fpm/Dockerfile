FROM thomasredstone/base:2.0.1  
# Install php-fpm  
RUN apt-get update -qq && apt-get -y upgrade  
RUN apt-get install -y -qq software-properties-common python-software-
properties language-pack-en-base  
RUN LC_ALL=en_GB.UTF-8 add-apt-repository ppa:ondrej/php  
  
RUN apt-get update && apt-get -y -qq install curl libcurl3 libcurl3-dev
php7.1-fpm php7.1-mysql php7.1-curl php7.1-json php7.1-mbstring php7.1-zip
php7.1-xml php7.1-sqlite wget php7.1-imap  
RUN usermod -u 1000 www-data  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
# Adding the configuration files  
RUN mkdir /run/php/ && chown -R www-data:www-data /run/php/  
ADD conf/www.conf /etc/php/7.1/fpm/pool.d/www.conf  
ADD conf/php-fpm.conf /etc/php/7.1/fpm/php-fpm.conf  
# Add the run script to run the service  
ADD run.sh /run.sh  
  
#add the volume for the application  
VOLUME /var/www/app  
  
# Expose the port 9000  
EXPOSE 9000  
# Run the run.sh script  
ENTRYPOINT [ "/bin/bash", "/run.sh"]  

