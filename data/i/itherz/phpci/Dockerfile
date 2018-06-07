FROM ubuntu:latest  
  
MAINTAINER Dmitrii Zolotov <dzolotov@herzen.spb.ru>  
  
RUN DEBIAN_FRONTEND=noninteractive  
  
RUN echo "ru_RU.UTF-8 UTF-8" >>/etc/locale.gen && apt-get update && apt-get
install -y locales && locale-gen && export LC_ALL=ru_RU.UTF-8 && \  
echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee
/etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
apt-get update && apt-get -o=APT::Force-LoopBreak=1 -u -y upgrade && apt-get
install -o=APT::Force-LoopBreak=1 -y oracle-java8-installer software-
properties-common python-software-properties python-setuptools wget curl
mysql-client maven jshon npm nodejs doxygen && \  
apt-get install -y --force-yes --allow-unauthenticated unzip php7.0-cli
php7.0-mbstring php7.0-zip php7.0-mysql php7.0-curl php7.0-ldap php7.0-gd
php7.0-imap php7.0-interbase php7.0-intl php7.0-mcrypt php7.0-xsl php7.0-json
php7.0-sybase php7.0-bz2 php-mongodb git && \  
cd /usr/bin && curl -sS https://getcomposer.org/installer | php && \  
mv /usr/bin/composer.phar /usr/bin/composer && chmod +x /usr/bin/composer &&
mkdir -p /var/www/html && \  
cd /var/www/html && rm -rf * && git clone https://github.com/it-herz/PHPCI .
&& git checkout pluggable-auth && \  
ln -s /root/.composer/vendor/bin/* /usr/bin && \  
mkdir -p /run/php && mkdir -p /var/lib/php/sessions && chmod 777 -R
/var/lib/php/sessions && \  
cd /var/www/html && \  
ln -s /usr/bin/nodejs /usr/bin/node && git config --global
url."https://".insteadOf git:// && npm install -g bower gulp && \  
apt-get clean && rm -rf /var/lib/apt/lists/* && \  
sed -i 's/error_reporting = .*/error_reporting = E_ALL \& ~E_NOTICE \&
~E_WARNING/' /etc/php/7.0/cli/php.ini  
  
ADD config.yml /var/www/html/PHPCI/config.yml  
  
ADD prephp.sh /  
ADD run.sh /  
  
# Supervisor Config  
RUN mkdir /var/log/supervisor/  
RUN /usr/bin/easy_install supervisor  
RUN /usr/bin/easy_install supervisor-stdout  
ADD supervisord.conf /etc/supervisord.conf  
  
ENV MYSQL_HOST mysql  
ENV MYSQL_USER root  
ENV MYSQL_PASSWORD root  
ENV MYSQL_DBNAME phpci  
ENV GITHUB_TOKEN ...  
ENV TIMEZONE GMT  
ENV URL http://changeme  
ENV GITHOST github.com  
ENV GITPORT 80  
ENV BEANSTALK_HOST beanstalk  
ENV BEANSTALK_QUEUE phpci  
ENV PATH $PATH:/var/www/html/vendor/bin  
  
WORKDIR /var/www/html/  
  
VOLUME /var/www/html/PHPCI/build/  
  
CMD ["supervisord","-n","-c","/etc/supervisord.conf"]  

