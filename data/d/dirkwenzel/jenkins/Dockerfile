FROM jenkins:2.46.1  
USER root  
  
#ENV MAVEN_VERSION 3.3.9  
#RUN cd /usr/local; wget -q -O -
http://mirrors.ibiblio.org/apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xvfz - && \  
# ln -sv /usr/local/apache-maven-$MAVEN_VERSION /usr/local/maven  
WORKDIR /tmp/files  
  
COPY bin/run.sh /usr/local/bin/  
RUN chmod a+x /usr/local/bin/run.sh && \  
## add dotdeb to apt sources list  
echo 'deb http://packages.dotdeb.org jessie all' >
/etc/apt/sources.list.d/dotdeb.list && \  
  
## add dotdeb key for apt  
curl http://www.dotdeb.org/dotdeb.gpg | apt-key add \- && \  
  
## upgrade to php 7  
apt-get update && apt-get install -y \  
apt-transport-https \  
php7.0 php7.0-cli php7.0-curl php7.0-gd php7.0-geoip php7.0-intl php7.0-json \  
php7.0-mbstring php7.0-mcrypt php7.0-mysql php7.0-opcache php7.0-readline
php7.0-xml php7.0-xsl php7.0-zip \  
ruby bundler && \  
## install composer  
curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer && chown -R jenkins.jenkins /usr/local/bin/composer  
  
  
USER jenkins  
CMD /usr/local/bin/run.sh  

