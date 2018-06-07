################################################################################  
# Base image  
################################################################################  
  
FROM kireevco/openresty:1.11.2.1-1.0.2j-1.11.33.4-rev-2  
MAINTAINER Dmitry Kireev <dmitry@kireev.co>  
  
ENV \  
DEBIAN_FRONTEND=noninteractive \  
TERM=xterm-color  
  
# Install base utils  
RUN apt-get update && apt-get install -my \  
wget \  
curl  
  
# Remove default nginx configs.  
RUN rm -f /etc/nginx/conf.d/*  
  
# Install HHVM Repo  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449  
RUN echo deb http://dl.hhvm.com/debian jessie main | tee
/etc/apt/sources.list.d/hhvm.list  
  
# Install NewRelic Repo  
RUN wget -O - https://download.newrelic.com/548C16BF.gpg | apt-key add -  
RUN echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list  
  
# Install packages  
RUN apt-get clean && apt-get update && apt-get install -my \  
supervisor \  
python python-pip python-dev \  
curl \  
wget \  
php5-curl \  
php5-fpm \  
php5-gd \  
php5-memcache \  
php5-memcached \  
php5-mysql \  
php5-mcrypt \  
php5-sqlite \  
php5-xdebug \  
hhvm \  
php-apc \  
cron \  
openjdk-7-jre \  
yui-compressor \  
tidy \  
newrelic-php5 \  
htop vim strace dstat mc mysql-client netcat  
  
# Install Cache Primer  
RUN wget https://cdn.pmylund.com/files/tools/ocp2/linux/ocp-2.7-amd64.tar.gz  
RUN tar -zxf ocp-2.7-amd64.tar.gz -C /opt  
  
# Install j2cli (will help us with config templating)  
RUN pip install j2cli && pip install j2cli[yaml]  
  

