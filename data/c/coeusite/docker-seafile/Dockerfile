FROM debian:stretch  
  
# Initially was based on work of Alessandro Viganò, Andreas Löffler
<andy@x86dev.com>  
MAINTAINER CoeusITE <coeusite@gmail.com>  
  
# Base system  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && apt-get upgrade -y && \  
apt-get install -y ca-certificates nginx net-tools wget curl supervisor apt-
utils && \  
apt-get install -y python2.7 python-setuptools python-imaging python-ldap
python-mysqldb python-memcache python-urllib3 && \  
apt-get clean all && \  
sed -i 's/^\\(\\[supervisord\\]\\)$/\1\nnodaemon=true/'
/etc/supervisor/supervisord.conf  
  
# Seafile  
RUN mkdir /opt/seafile/logs -p && \  
cd /opt/seafile/ && \  
wget https://download.seadrive.org/seafile-server_6.2.5_x86-64.tar.gz && \  
tar xzf seafile-server_*.tar.gz && \  
mkdir installed && \  
mv seafile-server_* installed  
  
# Nginx  
ADD seafile-nginx.conf /etc/nginx/sites-available/seafile  
# Supervisor  
ADD seafile-supervisord.conf /etc/supervisor/conf.d/seafile-supervisord.conf  
# bootstrap  
ADD bootstrap-data.sh /usr/local/sbin/bootstrap  
  
# Expose needed ports.  
EXPOSE 8080  
# Volumes  
VOLUME ["/etc/nginx", "/opt/seafile", "/etc/supervisor/conf.d"]  
  
# CMD  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]  
  
# docker build -t docker-seafile:stretch .  

