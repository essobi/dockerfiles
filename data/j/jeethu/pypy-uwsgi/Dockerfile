FROM jeethu/pypy:4.0.1  
MAINTAINER Jeethu Rao <jeethu@jeethurao.com>  
  
RUN set -e; \  
apt-get update; \  
apt-get -yq install wget supervisor gcc; \  
cd /tmp/; \  
pip install uwsgi==2.0.11.2 uwsgitop==0.9; \  
ln -s /usr/local/pypy-4.0.1-linux_x86_64-portable/bin/uwsgi* /usr/local/bin/;
\  
apt-get purge -yq wget; \  
apt-get -yq autoremove; \  
apt-get clean; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["/usr/bin/supervisord"]  

