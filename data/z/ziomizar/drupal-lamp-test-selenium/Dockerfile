# FROM ubuntu:14.04  
FROM elgalu/selenium:latest  
  
RUN sudo apt-get update  
RUN sudo apt-get install -y software-properties-common python-software-
properties  
RUN sudo add-apt-repository ppa:ondrej/php  
RUN sudo apt-get update  
RUN sudo apt-get -qq -y install apache2  
RUN sudo apt-get -qq -y install software-properties-common  
RUN sudo apt-get -qq -y install mariadb-server  
  
RUN sudo apt-get -qq --force-yes -y install php  
RUN sudo apt-get -qq --force-yes -y install php-mbstring  
RUN sudo apt-get -qq --force-yes -y install php-mcrypt  
RUN sudo apt-get -qq --force-yes -y install php-curl  
RUN sudo apt-get -qq --force-yes -y install php-xml  
RUN sudo apt-get -qq --force-yes -y install php-mysql  
RUN sudo apt-get -qq --force-yes -y install libapache2-mod-php  
  
RUN sudo apt-get -qq -y install git  
RUN sudo apt-get -y install openssh-server  
RUN sudo apt-get -qq -y install curl  
  
RUN sudo curl -sS https://getcomposer.org/installer | php  
RUN sudo mv composer.phar /usr/local/bin/composer  
RUN sudo ln -s /usr/local/bin/composer /usr/bin/composer  
RUN cd ~  
RUN wget https://phar.phpunit.de/phpunit-6.0.phar  
RUN chmod +x phpunit-6.0.phar  
RUN sudo mv phpunit-6.0.phar /usr/local/bin/phpunit  
RUN phpunit --version  
  
# install drush following http://docs.drush.org/en/master/install/  
RUN cd ~  
RUN sudo mkdir /home/seluser/.drush  
RUN sudo chown -Rv seluser /home/seluser/.drush  
RUN sudo chmod -Rv 664 /home/seluser/.drush  
RUN wget https://s3.amazonaws.com/files.drush.org/drush.phar  
RUN sudo chmod +x drush.phar  
RUN sudo mv drush.phar /usr/local/bin/drush  
RUN sudo chmod -Rv 777 /home/seluser/.drush  
RUN sudo chown -Rv seluser /home/seluser/.drush  
  
RUN sudo apt-get install -y -q software-properties-common wget  
RUN sudo add-apt-repository -y ppa:mozillateam/firefox-next  
RUN sudo wget -qO- https://deb.nodesource.com/setup_5.x | sudo bash -  
RUN sudo apt-get install -y nodejs  
RUN sudo wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub |
sudo apt-key add -  
RUN sudo su -c "echo 'deb http://dl.google.com/linux/chrome/deb/ stable main'
> /etc/apt/sources.list.d/google.list"  
RUN sudo apt-get update -y  
RUN sudo apt-get install -y -q --force-yes firefox  
RUN sudo apt-get install -y -q --force-yes google-chrome-beta  
# java  
RUN sudo add-apt-repository -y ppa:openjdk-r/ppa  
RUN sudo apt-get update  
RUN sudo apt-get install -y -q openjdk-7-jre-headless  
  
RUN sudo apt-get install -y -q nodejs  
RUN sudo apt-get install -y -q x11vnc  
RUN sudo apt-get install -y -q xvfb  
RUN sudo apt-get install -y -q xfonts-100dpi  
RUN sudo apt-get install -y -q xfonts-75dpi  
RUN sudo apt-get install -y -q xfonts-scalable  
RUN sudo apt-get install -y -q xfonts-cyrillic  
  
RUN sudo npm install -g selenium-standalone@5.0.0  
RUN sudo npm install -g phantomjs-prebuilt@2.1.4 && sudo selenium-standalone
install  
  
RUN export DISPLAY=:99  
RUN Xvfb :99 -shmem -screen 0 1366x768x16 &  
RUN x11vnc -passwd secret -display :99 -N -forever &  
  
USER seluser  
ENV HOME /home/seluser  
  

