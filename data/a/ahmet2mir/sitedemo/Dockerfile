FROM debian:wheezy  
MAINTAINER Ahmet Demir <ahmet2mir+github@gmail.com>  
  
ENV RELEASE wheezy  
ENV DEBIAN_FRONTEND noninteractive  
ENV SHELL /bin/bash  
  
RUN echo "deb http://ftp.fr.debian.org/debian $RELEASE main contrib non-free"
> /etc/apt/sources.list;\  
echo "deb http://ftp.debian.org/debian/ $RELEASE-updates main contrib non-
free" >> /etc/apt/sources.list;\  
echo "deb http://security.debian.org/ $RELEASE/updates main contrib non-free"
>> /etc/apt/sources.list  
  
RUN apt-get update  
  
RUN apt-get install -y --no-install-recommends apache2 php5 git  
  
ADD . /var/www  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl","-D","FOREGROUND"]  

