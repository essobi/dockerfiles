FROM phusion/baseimage  
MAINTAINER Thiago Taranto <ttaranto@gmail.com>  
MAINTAINER Aleksey Dorokhov <akeinhell@gmail.com>  
  
# ensure UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# change resolv.conf  
#RUN echo 'nameserver 8.8.8.8' > /etc/resolv.conf  
# setup  
ENV HOME /root  
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
CMD ["/sbin/my_init"]  
  
# nginx-php installation  
RUN DEBIAN_FRONTEND="noninteractive" add-apt-repository ppa:ondrej/php  
RUN DEBIAN_FRONTEND="noninteractive" apt-get update  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y upgrade  
RUN DEBIAN_FRONTEND="noninteractive" apt-get update --fix-missing  
RUN DEBIAN_FRONTEND="noninteractive" apt-cache policy search php7.1*  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install php7.1  
RUN DEBIAN_FRONTEND="noninteractive" apt-get -y install php7.1-fpm php7.1-intl
php7.1-common php7.1-cli php7.1-mysqlnd php7.1-mcrypt php7.1-curl
php7.1-bcmath php7.1-mbstring php7.1-soap php7.1-xml php7.1-zip php7.1-json
php7.1-imap php-xdebug php-pgsql  
  
# install nginx (full)  
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y nginx-full  
  
# install latest version of nodejs  
RUN DEBIAN_FRONTEND="noninteractive" apt-get install -y git  
  
ENV NVM_DIR /usr/local/.nvm  
ENV NODE_VERSION stable  
  
# Install nvm  
RUN apt-get install -y build-essential  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
  
RUN npm i -g yarn  
  
#cleanup  
RUN rm -rf /var/lib/apt/lists/*  
  
# install php composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN composer global require hirak/prestissimo  
  
# add build script (also set timezone to Americas/Sao_Paulo)  
RUN mkdir -p /root/setup  
ADD build/setup.sh /root/setup/setup.sh  
RUN chmod +x /root/setup/setup.sh  
RUN (cd /root/setup/; /root/setup/setup.sh)  
  
# copy files from repo  
ADD build/nginx.conf /etc/nginx/sites-available/default  
ADD build/.bashrc /root/.bashrc  
  
# disable services start  
RUN update-rc.d -f apache2 remove  
RUN update-rc.d -f nginx remove  
RUN update-rc.d -f php7.1-fpm remove  
  
# add startup scripts for nginx  
ADD build/nginx.sh /etc/service/nginx/run  
RUN chmod +x /etc/service/nginx/run  
  
# add startup scripts for php7.1-fpm  
ADD build/phpfpm.sh /etc/service/phpfpm/run  
RUN chmod +x /etc/service/phpfpm/run  
  
# set WWW public folder  
RUN mkdir -p /var/www/public  
ADD build/index.php /var/www/public/index.php  
  
RUN chown -R www-data:www-data /var/www  
RUN chmod 755 /var/www  
  
# set terminal environment  
ENV TERM=xterm  
  
# port and settings  
EXPOSE 80 443 9000  
# cleanup apt and lists  
RUN apt-get clean  
RUN apt-get autoclean  

