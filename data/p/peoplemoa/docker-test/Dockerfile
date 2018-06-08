FROM ubuntu:14.04  
  
RUN apt-get update  
RUN apt-get upgrade -y  
RUN apt-get install -y apache2 php5 php5-mysql php5-xdebug mysql-client
cronolog  
RUN apt-get install -y curl wget  
RUN apt-get install -y git  
  
# RUN apt-get install -y php-pear php5-dev  
# RUN apt-get install -y libcurl3-openssl-dev  
# RUN pecl install pecl_http  
# 한국시간으로 변경  
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime  
  
# 아파치 모듈 설치  
RUN a2enmod rewrite  
VOLUME ["/srv", "/etc/apache2/sites-available", "/etc/apache2/sites-enabled"]  
EXPOSE 80  
EXPOSE 443  
  
# php composer 설치  
# RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
# ADD user.sh /user.sh  
# RUN chmod +x /user.sh  
# RUN /user.sh  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT /entrypoint.sh  

