FROM ubuntu:14.04.2  
MAINTAINER Andres Torres Marroquin <andres.torres.marroquin@gmail.com>  
  
ENV LANG C.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
  
# Installing NGINX  
RUN apt-get update; \  
apt-get install -y nginx  
  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Installing supervisord  
RUN apt-get update && apt-get install -y supervisor  
RUN mkdir -p /var/log/supervisor  
  
# Installing PyPy 2.4.0  
RUN set -e; \  
umask 0022; \  
apt-get update; apt-get -yq install wget; \  
wget -q https://bitbucket.org/squeaky/portable-
pypy/downloads/pypy-2.4-linux_x86_64-portable.tar.bz2 -P /tmp/; \  
tar -xjf /tmp/pypy-2.4-linux_x86_64-portable.tar.bz2 -C /usr/local; \  
ln -s /usr/local/pypy-2.4-linux_x86_64-portable/bin/libpypy-c.so
/usr/lib/x86_64-linux-gnu/; \  
ldconfig; \  
wget -qO- 'https://bootstrap.pypa.io/get-pip.py' |
/usr/local/pypy-2.4-linux_x86_64-portable/bin/pypy; \  
/usr/local/pypy-2.4-linux_x86_64-portable/bin/pip install virtualenv; \  
ln -s /usr/local/pypy-2.4-linux_x86_64-portable/bin/* /usr/local/bin/; \  
rm /tmp/pypy-2.4-linux_x86_64-portable.tar.bz2; \  
apt-get purge -yq wget; \  
apt-get -yq autoremove; \  
apt-get autoclean  
  
# Installing postgresql headers and headers for PIL  
RUN apt-get update; \  
apt-get install -y postgresql-server-dev-all libfreetype6-dev libjpeg-dev
libpng-dev  
  
# Installing mongo shell  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10; \  
echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.0 main" |
sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.list; \  
apt-get update; \  
apt-get install -y mongodb-org-shell mongodb-org-tools  
  
# Starting up  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

