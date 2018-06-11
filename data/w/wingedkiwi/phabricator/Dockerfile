#  
# Docker image for running https://github.com/phacility/phabricator  
#  
FROM wingedkiwi/ubuntu-baseimage:master  
MAINTAINER Chi Vinh Le <cvl@winged.kiwi>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
  
# Change to different archive  
RUN mv /etc/apt/sources.list /etc/apt/sources.list.save && cat
/etc/apt/sources.list.save | sed 's/archive/de.archive/g' >
/etc/apt/sources.list  
  
# Add nginx ppa  
RUN add-apt-repository ppa:nginx/stable  
# Add nodejs ppa  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -  
  
# TODO: review this dependency list  
RUN apt-get install -y \  
nodejs \  
build-essential \  
nginx \  
php5-fpm \  
php5-cli \  
php5-mysql \  
php5-curl \  
php5-gd \  
php5-ldap \  
php5-json \  
php-apc \  
php5-apcu \  
python-pygments \  
exim4 \  
mercurial \  
subversion \  
git \  
curl \  
tar \  
openssh-server \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# For some reason phabricator doesn't have tagged releases. To support  
# repeatable builds use the latest SHA  
ADD download.sh /opt/download.sh  
WORKDIR /opt  
RUN bash download.sh phacility phabricator 256fd47f2a  
RUN bash download.sh phacility arcanist ac28f951d6  
RUN bash download.sh phacility libphutil 4348ceaa54  
RUN bash download.sh PHPOffice PHPExcel 372c7cbb69  
  
# Create nginx user and group  
RUN echo "nginx:x:497:495:user for nginx:/var/lib/nginx:/bin/false" >>
/etc/passwd  
RUN echo "nginx:!:495:" >> /etc/group  
  
# Add user  
RUN echo "git:x:2000:2000:user for phabricator:/opt/phabricator:/bin/bash" >>
/etc/passwd  
RUN echo "wwwgrp-phabricator:!:2000:nginx" >> /etc/group  
  
# Setup aphlict  
# Add aphlict log  
RUN touch /var/log/aphlict.log && chown git:wwwgrp-phabricator
/var/log/aphlict.log  
# Install aphlict dependencies  
RUN cd /opt/phabricator/support/aphlict/server && export HOME=`pwd` && npm
install ws  
# Copy runit file  
RUN mkdir /etc/service/50-aphlict  
COPY services/aphlict/aphlict.runit /etc/service/50-aphlict/run  
  
# Setup syslog  
COPY services/syslog-ng/syslog-ng.conf /etc/syslog-ng/syslog-ng.conf  
  
# Setup sshd  
COPY services/sshd/sshd_config /etc/ssh/sshd_config  
COPY services/sshd/phabricator-ssh-hook.sh /etc/ssh/phabricator-ssh-hook.sh  
RUN dpkg-reconfigure openssh-server  
RUN mkdir /etc/service/20-sshd  
RUN mkdir /var/run/sshd  
COPY services/sshd/sshd.runit /etc/service/20-sshd/run  
  
# Setup exim  
RUN mkdir /etc/service/20-exim  
COPY services/exim/exim.runit /etc/service/20-exim/run  
COPY services/exim/update-exim4.conf.conf /etc/exim4/update-exim4.conf.conf  
  
# Setup phabricator  
RUN mkdir -p /opt/phabricator/conf/local /var/repo  
  
# Setup php5-fpm  
RUN mkdir /etc/service/30-php5-fpm  
COPY services/php5-fpm/php.ini /etc/php5/fpm/php.ini  
COPY services/php5-fpm/php-fpm.conf /etc/php5/fpm/php-fpm.conf  
COPY services/php5-fpm/php5-fpm.runit /etc/service/30-php5-fpm/run  
  
# Setup nginx  
RUN mkdir /etc/service/40-nginx  
COPY services/nginx/nginx.conf /etc/nginx/nginx.conf  
COPY services/nginx/fastcgi.conf /etc/nginx/fastcgi.conf  
COPY services/nginx/nginx.runit /etc/service/40-nginx/run  
  
# Setup phd  
RUN mkdir /etc/service/50-phd  
COPY services/phd/phd.runit /etc/service/50-phd/run  
  
# Copy init scripts  
COPY init/ /etc/my_init.d/  
  
EXPOSE 80  
ENTRYPOINT ["/sbin/my_init"]  

