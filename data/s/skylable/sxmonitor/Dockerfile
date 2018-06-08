FROM centos:centos7  
MAINTAINER Skylable Dev-Team <dev-team@skylable.com>  
  
# Install deps  
RUN yum clean all && \  
yum -y update && \  
yum -y install epel-release && \  
yum clean all;  
  
RUN yum -y install supervisor \  
gcc make automake autoconf \  
python-pip python-devel \  
nginx php-fpm ssmtp  
  
# temp fix for https://github.com/docker/hub-feedback/issues/461  
RUN yum -y install nagios nagios-plugins-ping || true  
  
RUN yum -y install git fcgi-devel && \  
cd /usr/local/src/ && \  
git clone git://github.com/gnosek/fcgiwrap.git && \  
cd fcgiwrap && \  
autoreconf -i && \  
./configure && \  
make && \  
make install  
  
# install deps  
RUN pip install sxclient nagiosplugin  
  
RUN mkdir -p /srv/logs/supervisor /var/log/nagios/rw/ \  
&& chown nagios:nagios /var/log/nagios/rw/ \  
&& chmod 770 /var/log/nagios/rw/ \  
&& chmod u+s /usr/bin/ping  
  
COPY php-fpm-www.conf /etc/php-fpm.d/www.conf  
COPY nginx.conf /etc/nginx/  
COPY nginx-sxmonitor.conf /etc/nginx/conf.d/  
  
# copy sxmonitor app  
#COPY sxmonitor/ /srv/sxmonitor  
ADD sxmonitor/templates /srv/sxmonitor/templates/  
ADD sxmonitor/*.sh sxmonitor/*.py /srv/sxmonitor/  
ADD sxmonitor/plugins/check_* /usr/lib64/nagios/plugins/  
ADD config.inc.php /usr/share/nagios/html/config.inc.php  
  
# config files  
COPY supervisord.conf /etc/supervisor/  
COPY run.sh /  
  
EXPOSE 80 443  
CMD ["/run.sh"]  
  

