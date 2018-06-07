FROM baszczewski/development  
MAINTAINER Marcin Baszczewski <marcin@baszczewski.pl>  
  
# apache2  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq apache2  
  
# mariadb  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq mariadb-server  
  
# ruby gems  
RUN gem install sass compass rmagick stringex  
  
# jekyll  
RUN gem install jekyll jekyll-assets jekyll-sitemap jekyll-feed jekyll-
paginate s3_website  
  
# php  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq php7.0 php7.0-mysql
php7.0-curl php7.0-json php7.0-cli php7.0-cgi php7.0-gd php7.0-zip
php7.0-mbstring php7.0-mcrypt php7.0-xsl php7.0-intl libapache2-mod-php7.0  
  
# additional packages for zephir  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq php7.0-dev re2c
libpcre3-dev php-apcu php-bcmath  
  
# nodejs  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq nodejs npm nodejs-
legacy  
  
# java  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq openjdk-8-jre  
  
# zephir  
WORKDIR /tmp  
RUN git clone https://github.com/phalcon/zephir  
WORKDIR zephir  
RUN ./install -c  
  
# composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# setup npm packages globally  
RUN sudo npm install -g gulp grunt grunt-cli bower forever coffee-script
typescript  
  
# exposed variables  
ENV MARIADB_USER admin  
ENV MARIADB_PASS **Random**  
ENV HOME /home/user/  
  
# volumes  
VOLUME ["/www", "/db"]  
  
# working directory  
WORKDIR /www  
  
# copy files  
ADD prepare.sh /opt/prepare.sh  
ADD prepare_composer.sh /opt/prepare_composer.sh  
ADD run.sh /opt/run.sh  
ADD my.cnf /tmp/my.cnf  
ADD php.ini /tmp/php.ini  
ADD phpinfo.php /tmp/phpinfo.php  
  
# allow execute scripts  
RUN chmod a+x /opt/prepare.sh  
RUN chmod a+x /opt/run.sh  
  
# expose ports  
EXPOSE 80 3306 4040 4000  
# process prepare.sh (only once)  
RUN /opt/prepare.sh  
  
# add user to sudo  
RUN adduser --disabled-password --home=/home/user --gecos "" user  
RUN adduser user sudo  
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
# change user  
USER user  
# process prepare_composer.sh (only once)  
RUN /opt/prepare_composer.sh  
  
# process run.sh as default command (every time)  
CMD ["/opt/run.sh"]  

