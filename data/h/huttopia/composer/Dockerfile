FROM cedvan/ubuntu:14.04.20150428  
MAINTAINER Cédric Vanet <dev@cedvan.com>  
MAINTAINER Maxime Sifflet <maxime.sifflet@huttopia.com>  
  
# Install git  
RUN apt-get update -qq \  
&& apt-get install -qqy git  
  
# install HHVM  
RUN wget -O - http://dl.hhvm.com/conf/hhvm.gpg.key | apt-key add -  
RUN echo deb http://dl.hhvm.com/ubuntu trusty main | tee
/etc/apt/sources.list.d/hhvm.list  
RUN apt-get update -qq && apt-get install -qqy hhvm  
  
# Downgrade HHVM to 3.2.0 (Fix issue
https://github.com/facebook/hhvm/issues/3797)  
RUN wget
http://dl.hhvm.com/ubuntu/pool/main/h/hhvm/hhvm_3.2.0~trusty_amd64.deb  
RUN dpkg -i hhvm_3.2.0~trusty_amd64.deb  
RUN rm -f hhvm_3.2.0~trusty_amd64.deb  
  
# Configuration HHVM  
RUN echo "date.timezone = Europe/Paris" >> /etc/hhvm/php.ini  
COPY assets/config.hdf /etc/hhvm/config.hdf  
  
# install composer  
RUN wget -O /usr/local/bin/composer -q http://getcomposer.org/composer.phar  
RUN chmod +x /usr/local/bin/composer  
  
# Launch composer cith hhvm  
ADD assets/composer-hhvm bin/composer-hhvm  
RUN chmod +x /bin/composer-hhvm  
  
# Update Composer  
RUN /bin/composer-hhvm self-update  
  
WORKDIR /src  
  
ENTRYPOINT ["composer-hhvm"]  

