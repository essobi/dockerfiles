FROM hoanglala/ubuntu-apache  
  
MAINTAINER Hoang Nguyen <nbhoangit@gmail.com>  
  
RUN apt-get update -y && \  
apt-get install php7.0 libapache2-mod-php7.0 vim -y && \  
apt-get clean && \  
rm -rf \var\lib\lists\\*  
  
COPY default.conf /etc/apache2/sites-available/000-default.conf

