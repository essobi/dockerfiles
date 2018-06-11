FROM phusion/baseimage:0.9.15  
ENV HOME /root  
COPY . /build  
WORKDIR /tmp  
  
RUN add-apt-repository -y ppa:nginx/stable  
RUN apt-get update  
  
# base env  
RUN apt-get install -y --force-yes git curl make telnet nginx php5-fpm  
  
# PHP  
RUN apt-get install -y --force-yes php5-cli php5-sqlite php5-curl php5-gd
php5-mcrypt php5-intl  
  
RUN ln -s /etc/php5/mods-available/mcrypt.ini
/etc/php5/cli/conf.d/20-mcrypt.ini  
RUN ln -s /etc/php5/mods-available/mcrypt.ini
/etc/php5/fpm/conf.d/20-mcrypt.ini  
  
# MySQL  
RUN apt-get install -y --force-yes mysql-client php5-mysql  
  
# MongoDB  
RUN apt-get install -y --force-yes php5-mongo mongodb-clients  
  
# ruby & rvm (not necessary)  
RUN apt-get install -y --force-yes git-core curl zlib1g-dev build-essential
libssl-dev libreadline-dev libyaml-dev libsqlite3-dev sqlite3 libxml2-dev
libxslt1-dev libcurl4-openssl-dev python-software-properties libgdbm-dev
libncurses5-dev automake libtool bison libffi-dev  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -L https://get.rvm.io | bash -s stable  
RUN source /etc/profile.d/rvm.sh  
RUN echo "source /etc/profile.d/rvm.sh" >> ~/.bashrc  
RUN rvm install 2.1.2  
RUN rvm use 2.1.2 –default  
RUN gem install compass  
RUN gem install sass  
  
# nodejs  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get install -y --force-yes nodejs  
  
# composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
RUN echo "Host bitbucket.org\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config  
RUN echo "Host github.com\n\tStrictHostKeyChecking no\n" >> ~/.ssh/config  
  
EXPOSE 8000 80  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/fpm/php.ini  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/cli/php.ini  
RUN sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-
fpm.conf  
RUN sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini  
  
#RUN mkdir -p /var/www  
ADD _nginx/default /etc/nginx/sites-available/default  
RUN mkdir /etc/service/nginx  
ADD _nginx/nginx.sh /etc/service/nginx/run  
RUN chmod +x /etc/service/nginx/run  
RUN mkdir /etc/service/phpfpm  
ADD _nginx/phpfpm.sh /etc/service/phpfpm/run  
RUN chmod +x /etc/service/phpfpm/run  
  
# workround for boot2docker / Kitematic  
RUN usermod -u 1000 www-data  
  
RUN mkdir -p /data/public && echo "<?php phpinfo();" > /data/public/index.php  
VOLUME /data  
  
#CMD [ "/usr/bin/php", "-S 127.0.0.1:8000 -t ./public" ]  
WORKDIR /data  
CMD ["/sbin/my_init"]  

