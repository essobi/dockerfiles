FROM jenkins:latest  
MAINTAINER Jonathan Hawk <jonathan@appertly.com>  
  
USER root  
ENV HHVM_VERSION 3.8.0~jessie  
ENV PATH /var/jenkins_home/.composer/vendor/bin:$PATH  
  
# Install all the crap we need  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449 \  
&& echo deb http://dl.hhvm.com/debian jessie main | tee
/etc/apt/sources.list.d/hhvm.list \  
&& apt-get update && apt-get install -y --no-install-recommends ant
hhvm=$HHVM_VERSION \  
&& echo "date.timezone = UTC" >> /etc/hhvm/php.ini \  
&& echo "hhvm.libxml.ext_entity_whitelist = file" >> /etc/hhvm/php.ini \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -O http://getcomposer.org/composer.phar \  
&& chmod +x composer.phar \  
&& mv composer.phar /usr/local/bin/composer  
  
# Install some Jenkins plugins  
ADD plugins.txt /plugins.txt  
RUN plugins.sh /plugins.txt \  
&& rm /plugins.txt \  
&& mkdir -p /usr/share/jenkins/ref/jobs/php-template \  
&& curl -O https://raw.githubusercontent.com/sebastianbergmann/php-jenkins-
template/master/config.xml \  
&& mv config.xml /usr/share/jenkins/ref/jobs/php-template  
ADD composer.groovy /usr/share/jenkins/ref/init.groovy.d/composer.groovy  
  
USER jenkins  

