FROM ubuntu:14.04.4  
MAINTAINER Dmytro Boiko <whiteagleg@gmail.com>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
#Create docker user  
RUN mkdir -p /var/www  
RUN mkdir -p /home/docker  
RUN useradd -d /home/docker -s /bin/bash -M -N -G www-data,sudo,root docker  
RUN echo docker:docker | chpasswd  
RUN usermod -G www-data,users www-data  
RUN chown -R docker:www-data /var/www  
RUN chown -R docker:www-data /home/docker  
  
#install Software  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
RUN apt-get update && apt-get upgrade -y  
RUN dpkg-reconfigure tzdata  
RUN apt-get install -y software-properties-common python-software-properties \  
git git-core vim nano mc nginx screen curl unzip wget \  
supervisor memcached htop tmux zip \  
npm nodejs-legacy python-sphinx ruby  
RUN npm install -g grunt-cli bower  
COPY configs/nginx/default /etc/nginx/sites-available/default  
RUN gem install net-ssh -v 2.9.2  
RUN gem install capifony  
  
#Install PHP  
RUN apt-get install -y language-pack-en-base \  
php5 php5-fpm php5-cli php5-common php5-intl \  
php5-json php5-mysql php5-gd php5-imagick \  
php5-curl php5-mcrypt php5-dev \  
php5-memcached php5-memcache php-pear  
RUN pecl install xdebug  
RUN rm /etc/php5/cli/php.ini  
RUN rm /etc/php5/fpm/php.ini  
RUN rm /etc/php5/fpm/pool.d/www.conf  
COPY configs/php/www.conf /etc/php5/fpm/pool.d/www.conf  
COPY configs/php/php.ini /etc/php5/cli/php.ini  
COPY configs/php/php.ini /etc/php5/fpm/php.ini  
COPY configs/php/xdebug.ini /etc/php5/mods-available/xdebug.ini  
RUN ln -s /etc/php5/mods-available/xdebug.ini
/etc/php5/fpm/conf.d/20-xdebug.ini  
RUN ln -s /etc/php5/mods-available/xdebug.ini
/etc/php5/cli/conf.d/20-xdebug.ini  
  
# Install MariaDB.  
RUN echo "mariadb-server-10.0 mysql-server/root_password password root" | sudo
debconf-set-selections  
RUN echo "mariadb-server-10.0 mysql-server/root_password_again password root"
| sudo debconf-set-selections  
RUN \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
0xcbcb082a1bb943db && \  
echo "deb http://mariadb.mirror.iweb.com/repo/10.0/ubuntu `lsb_release -cs`
main" > /etc/apt/sources.list.d/mariadb.list && \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y mariadb-server && \  
rm -rf /var/lib/apt/lists/* && \  
sed -i 's/^\\(bind-address\s.*\\)/# \1/' /etc/mysql/my.cnf && \  
echo "mysqld_safe &" > /tmp/config && \  
echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config && \  
echo "mysql -uroot -proot -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\"
WITH GRANT OPTION;'" >> /tmp/config && \  
bash /tmp/config && \  
rm -f /tmp/config  
  
# SSH service  
RUN apt-get update && apt-get install -y openssh-server openssh-client  
RUN echo 'root:root' | chpasswd  
#change 'pass' to your secret password  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
#configs bash start  
COPY configs/autostart.sh /root/autostart.sh  
RUN chmod +x /root/autostart.sh  
COPY configs/bash.bashrc /etc/bash.bashrc  
COPY configs/.bashrc /root/.bashrc  
COPY configs/.bashrc /home/docker/.bashrc  
  
#Install locale  
RUN locale-gen en_US en_US.UTF-8 uk_UA uk_UA.UTF-8  
RUN dpkg-reconfigure locales  
  
#Install Java 8  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
# Accept license non-iteractive  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | sudo /usr/bin/debconf-set-selections  
RUN apt-get install -y oracle-java8-installer \  
oracle-java8-set-default  
RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" | sudo tee -a /etc/environment  
RUN export JAVA_HOME=/usr/lib/jvm/java-8-oracle  
  
#ant install  
RUN sudo apt-get install -y ant  
  
#Autocomplete symfony2  
COPY configs/files/symfony2-autocomplete.bash
/etc/bash_completion.d/symfony2-autocomplete.bash  
  
#Composer  
RUN cd /home  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin/ --filename=composer  
RUN chmod 777 /usr/local/bin/composer  
  
#Code standart  
RUN composer global require "squizlabs/php_codesniffer=*"  
RUN composer global require "sebastian/phpcpd=*"  
RUN composer global require "phpmd/phpmd=@stable"  
RUN cd /usr/bin && ln -s ~/.composer/vendor/bin/phpcpd  
RUN cd /usr/bin && ln -s ~/.composer/vendor/bin/phpmd  
RUN cd /usr/bin && ln -s ~/.composer/vendor/bin/phpcs  
  
#etcKeeper  
RUN mkdir -p /root/etckeeper  
COPY configs/etckeeper.sh /root/etckeeper.sh  
COPY configs/files/etckeeper-hook.sh /root/etckeeper/etckeeper-hook.sh  
RUN chmod +x /root/etckeeper/*.sh  
RUN chmod +x /root/*.sh  
RUN /root/etckeeper.sh  
  
# Define mountable directories.  
VOLUME ["/etc/mysql", "/var/lib/mysql"]  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD ["mysqld_safe"]  
  
#open ports  
EXPOSE 80 22 9000 3306  

