FROM ubuntu:trusty-20150427  
MAINTAINER Likol <likol@likol.idv.tw>  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv
8B3981E7A6852F782CC4951600A6F0A3C300EE8C \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv
14AA40EC0831756756D7F66C4F4EA0AAE5267A6C \  
&& echo "deb http://ppa.launchpad.net/nginx/stable/ubuntu trusty main " >>
/etc/apt/sources.list \  
&& echo "deb http://ppa.launchpad.net/ondrej/php5-5.6/ubuntu trusty main " >>
/etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y nano supervisor logrotate locales \  
nginx openssh-server mysql-client git-core \  
php5-fpm php5-apcu php5-mysql php5-curl php5-gd python-pygments \  
&& update-locale LANG=C.UTF-8 LC_MESSAGES=POSIX \  
&& locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure locales \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 22  
EXPOSE 80  
VOLUME ["/var/log/phd", "/var/phd"]  
  
COPY assets/ /opt/assets/  
RUN chmod 755 /opt/assets/app/install  
RUN /opt/assets/app/install  
  
WORKDIR /opt/phabricator  
  
CMD ["./init"]

