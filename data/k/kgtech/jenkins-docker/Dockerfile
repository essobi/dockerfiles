FROM php:5-fpm  
  
RUN apt-get update && apt-get install -y \  
libpng-dev \  
libcurl4-gnutls-dev \  
libmcrypt-dev \  
libicu-dev \  
libxml2-dev \  
libxslt-dev \  
curl \  
git \  
openjdk-7-jdk \  
ant \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install gd curl \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-install mysql pdo pdo_mysql \  
&& docker-php-ext-install soap gettext calendar zip \  
&& docker-php-ext-install intl \  
&& docker-php-ext-install xsl \  
&& pecl install xdebug  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN curl -LsS http://phpdox.de/releases/phpdox.phar -o /usr/local/bin/phpdox  
RUN chmod a+x /usr/local/bin/phpdox  
  
RUN curl -LsS http://mirrors.jenkins-ci.org/war/2.20/jenkins.war -o
/opt/jenkins.war  
RUN chmod 644 /opt/jenkins.war  
ENV JENKINS_HOME /jenkins  
  
VOLUME /jenkins  
  
WORKDIR /jenkins  
  
ENTRYPOINT ["java", "-jar", "/opt/jenkins.war"]  
EXPOSE 8080  
CMD [""]

