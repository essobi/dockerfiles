FROM ubuntu:14.04  
  
RUN apt-get update  
RUN apt-get upgrade  
RUN apt-get install -y apache2 php5 php5-mysql mysql-client  
RUN apt-get install -y curl wget  
RUN apt-get install -y git  
  
# RUN apt-get install -y php-pear php5-dev  
# RUN apt-get install -y libcurl3-openssl-dev  
# RUN pecl install pecl_http  
ADD entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
# 한국시간으로 변경  
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime  
  
  
EXPOSE 80  
EXPOSE 443  
  
ENTRYPOINT /entrypoint.sh  

