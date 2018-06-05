FROM ubuntu:14.04  
MAINTAINER Dmitry Sinev <astartsky@gmail.com>  
ENV DEBIAN_FRONTEND=noninteractive \  
REFRESHED_AT=2015_08_31 \  
TERM=xterm  
  
# set locale  
RUN dpkg-reconfigure locales && \  
locale-gen ru_RU.UTF-8 && \  
/usr/sbin/update-locale LANG=ru_RU.UTF-8  
  
# install custom repositories  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key E5267A6C  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties && \  
add-apt-repository -y ppa:ondrej/mysql-5.6  
  
RUN apt-get update && apt-get install -y \  
supervisor \  
mysql-server \  
nano  
  
# configure mysql  
ADD mysql.sh /mysql.sh  
  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf;  
  
# configure supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
VOLUME ["/var/lib/mysql"]  
WORKDIR /var/lib/mysql  
  
EXPOSE 3306  
CMD ["/usr/bin/supervisord"]  

