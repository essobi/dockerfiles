FROM debian:wheezy  
MAINTAINER Oliver Soell <oliver@soell.net>  
  
ENV COLLECTD_VERSION 5.5.0  
RUN apt-get update -y && \  
apt-get install -y build-essential libcurl4-openssl-dev libyajl-dev btrfs-
tools curl python-jinja2 && \  
cd /opt && \  
curl -sL http://collectd.org/files/collectd-${COLLECTD_VERSION}.tar.gz | tar
zx && \  
cd collectd-${COLLECTD_VERSION} && \  
./configure --sysconfdir=/etc --prefix=/usr && \  
make && \  
make install && \  
cd .. && \  
rm -rf collectd-${COLLECTD_VERSION} && \  
apt-get remove -y --purge build-essential libcurl4-openssl-dev && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists  
  
# Override required!  
ENV HOSTNAME default  
  
# Env vars which represent multiple items are comma-separated  
# Builtins:  
# ENV DF_MOUNTS # e.g. /, /data  
# ENV DISK_DISKS # e.g. xvda, xvdb  
# Additions:  
# ENV BTRFS_MOUNTS # e.g. /var/lib/docker/btrfs, /data  
# ENV RIAK_STATS_URL # e.g. http://localhost:8098/stats  
# -> Librato  
# ENV LIBRATO_EMAIL  
# ENV LIBRATO_TOKEN  
ADD collectd.conf.tpl /etc/collectd.conf.tpl  
ADD collectd.d /etc/collectd.d  
ADD collectd-render.py /usr/local/bin/collectd-render.py  
ADD df-btrfs.py /usr/local/bin/df-btrfs.py  
ADD docker-start.sh /docker-start.sh  
  
ENTRYPOINT ["/docker-start.sh"]  
CMD ["collectd", "-f"]  

