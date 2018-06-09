FROM ubuntu:17.10  
# Setup common packages, repo info, etc  
RUN apt-get update  
RUN apt-get dist-upgrade -y  
RUN apt-get install -y whois sudo vim htop software-properties-common python-
software-properties sendmail git iproute iputils-ping  
RUN LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php  
RUN apt-get update  
  
# Install packages  
RUN apt-get install -y apache2 apache2-bin apache2-data apache2-utils
libapache2-mod-fcgid php5.6-bcmath php5.6-cli php5.6-common php5.6-curl
php5.6-fpm php5.6-gd php5.6-intl php5.6-json php5.6-mbstring php5.6-mcrypt
php5.6-mysql php5.6-opcache php5.6-readline php5.6-soap php5.6-xml php5.6-xsl
php5.6-zip php-xdebug  
  
# Setup PHP  
RUN mkdir /run/php  
RUN touch /run/php/php-fpm.sock  
RUN echo "alias php-debug='php -d xdebug.remote_autostart=1'" >
/etc/bash.bashrc  
  
# Setup apache  
RUN ln -s /etc/apache2/mods-available/proxy.conf /etc/apache2/mods-
enabled/proxy.conf  
RUN ln -s /etc/apache2/mods-available/proxy.load /etc/apache2/mods-
enabled/proxy.load  
RUN ln -s /etc/apache2/mods-available/headers.load /etc/apache2/mods-
enabled/headers.load  
RUN ln -s /etc/apache2/mods-available/proxy_fcgi.load /etc/apache2/mods-
enabled/proxy_fcgi.load  
RUN ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-
enabled/rewrite.load  
  
# Create new user  
RUN useradd -m -p `mkpasswd "inchoo"` -s /bin/bash inchoo  
RUN adduser inchoo sudo  
RUN ln -s /var/www/html /home/inchoo/html  
RUN echo 'debug="php -d xdebug.remote_autostart=On"' >> /home/inchoo/.bashrc  
  
# Add custom configuration  
ADD config/fpm.conf /etc/php/5.6/fpm/pool.d/www.conf  
  
# Add custom scripts  
ADD start.sh /start.sh  
ADD scripts/robo.phar /usr/bin/robo  
ADD scripts/composer.phar /usr/bin/composer  
ADD scripts/n98-magerun.phar /usr/bin/n98-magerun  
ADD scripts/n98-magerun2.phar /usr/bin/n98-magerun2  
  
RUN chmod 755 /start.sh  
RUN chmod 755 /usr/bin/robo  
RUN chmod 755 /usr/bin/composer  
RUN chmod 755 /usr/bin/n98-magerun  
RUN chmod 755 /usr/bin/n98-magerun2  
  
# Cleanup  
RUN apt-get autoremove -y  
RUN apt-get clean  
  
CMD ["/start.sh"]  

