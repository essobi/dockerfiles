# michaloo/webdev  
#  
# VERSION 0.0.1  
FROM ubuntu:14.04  
RUN apt-get update -y && \  
apt-get install -y curl git && \  
apt-get clean  
  
RUN apt-get install apache2 -y && \  
apt-get clean  
  
RUN apt-get install php5-cli php5-gd php5-mysql php5-mcrypt libapache2-mod-
php5 php5-xdebug -y && \  
apt-get clean  
  
RUN curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
RUN curl -L https://raw.github.com/wp-cli/builds/gh-pages/phar/wp-cli.phar >
/usr/local/bin/wp && \  
chmod +x /usr/local/bin/wp  
  
RUN echo 'deb http://ppa.launchpad.net/chris-lea/node.js/ubuntu precise main'
> /etc/apt/sources.list.d/nodejs.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C7917B12 && \  
apt-get update -y && \  
apt-get install nodejs -y && \  
apt-get clean && \  
npm install -g grunt-cli bower gulp  
  
RUN a2enmod rewrite  
  
EXPOSE 80  
ENTRYPOINT [ "/bin/bash" ]  
  
CMD [ "/start.sh" ]  
  
ADD ./start.sh /start.sh  

