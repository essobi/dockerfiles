FROM fedora:21  
MAINTAINER Stas Rudakou "stas@garage22.net"  
ENV SELF_PREFIX=ttrss  
  
RUN yum -y update; yum clean all;  
RUN yum -y install curl php php-mbstring php-pgsql php-xml tar uwsgi uwsgi-
plugin-php  
RUN mkdir -p /opt/docroot/$SELF_PREFIX && \  
cd /opt/docroot/$SELF_PREFIX && \  
curl -L https://api.github.com/repos/gothfox/Tiny-Tiny-RSS/tarball/master |
tar -xz --strip-components=1 && \  
chown uwsgi: -R .  
  
ADD uwsgi.ini /opt/uwsgi.ini  
ADD config.php /opt/docroot/$SELF_PREFIX/config.php  
  
EXPOSE 80  
WORKDIR /opt/docroot  
CMD uwsgi --ini /opt/uwsgi.ini  

