FROM miko2u/web  
MAINTAINER miko@cafelounge.net  
  
# packages  
ADD setup/*.php /usr/share/fuelphp-1.7.2-config/  
ADD setup/development /usr/share/fuelphp-1.7.2-config/development  
ADD setup/test /usr/share/fuelphp-1.7.2-config/test  
ADD setup/staging /usr/share/fuelphp-1.7.2-config/staging  
ADD setup/production /usr/share/fuelphp-1.7.2-config/production  
RUN yum -y install tar patch sudo \  
&& yum clean all \  
&& cd /tmp \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/bin/composer \  
&& cd /usr/share/ \  
&& composer create-project fuel/fuel:dev-1.7/master fuelphp-1.7.2 \  
&& useradd www \  
&& echo "www:www" | chpasswd \  
&& echo 'www ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/www \  
&& chown -R www:www /usr/share/fuelphp-1.7.2 /usr/share/fuelphp-1.7.2-config \  
&& chkconfig nginx on \  
&& chkconfig php-fpm on \  
&& rm -rf /tmp/*  
  
# configure  
ADD nginx/* /etc/nginx/conf.d/  
  
# startup  
ADD boot/* /boot/  
RUN chmod 700 /boot/prepare  

