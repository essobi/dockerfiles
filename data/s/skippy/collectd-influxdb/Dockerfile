# we use an unstable version of debian to get the latest collectd  
# without having to have the overhead of compiling it ourselves  
#  
#inspired by  
# https://github.com/andreasjansson/docker-collectd-write-graphite  
# https://github.com/ejholmes/docker-collectd  
#  
FROM debian:jessie  
MAINTAINER Adam Greene <adam.greene@gmail.com>  
  
RUN apt-get update -y && \  
apt-get install -y -q --no-install-recommends \  
collectd && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# add a fake mtab for host disk stats  
ADD etc_mtab /etc/mtab  
  
ADD confd-custom-linux-amd64 /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd  
  
ADD collectd.toml /etc/confd/conf.d/collectd.toml  
ADD collectd.conf.tmpl /etc/confd/templates/collectd.conf.tmpl  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD ["/run.sh"]  
  

