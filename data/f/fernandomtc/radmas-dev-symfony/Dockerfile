FROM fernandomtc/radmas-iyc-common  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# install python  
RUN \  
apt-get update && \  
apt-get install -y python python-dev python-pip python-virtualenv  
  
# install nodejs  
RUN \  
cd /tmp && \  
wget http://nodejs.org/dist/v0.10.36/node-v0.10.36-linux-x64.tar.gz && \  
tar -C /usr/local \--strip-components 1 -xzf node-v0.10.36-linux-x64.tar.gz &&
\  
cd /tmp && \  
rm -rf /tmp/node-v* && \  
npm install -g npm  
  
ENV PATH node_modules/.bin:$PATH  
ENV NODE_PATH /usr/local/lib/node_modules  
  
# install grunt and bower globally  
RUN \  
npm install -g bower grunt-cli  
  
RUN apt-get update && apt-get install -y awscli  
  
# install Java  
RUN \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer && \  
rm -rf /var/cache/oracle-jdk7-installer  
  
# define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
# install sqlite3  
RUN \  
apt-get update && \  
apt-get -y install libsqlite3-dev  
  
RUN gem install bundle mailcatcher --no-rdoc --no-ri  
RUN gem install net-ssh -v 2.9.2 --no-rdoc --no-ri  
RUN gem install capistrano -v 3.4.0 --no-rdoc --no-ri  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# install phpmetrics  
RUN wget
https://github.com/Halleck45/PhpMetrics/raw/master/build/phpmetrics.phar && \  
chmod +x phpmetrics.phar && \  
mv phpmetrics.phar /usr/local/bin/phpmetrics  
  
# install php-code-fixer  
RUN wget http://get.sensiolabs.org/php-cs-fixer.phar -O php-cs-fixer && \  
chmod a+x php-cs-fixer && \  
mv php-cs-fixer /usr/local/bin/php-cs-fixer  
  
# install supervisor daemon  
RUN apt-get update && apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
  
# install sudo  
RUN \  
apt-get update && \  
apt-get -y install sudo  
  
# install SSH  
RUN \  
apt-get update && apt-get install -y openssh-server  
  
RUN \  
rm -rf /var/lib/apt/lists/*  
  
CMD /bin/bash  

