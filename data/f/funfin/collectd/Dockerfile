FROM debian:jessie  
  
MAINTAINER OiSiS (https://github.com/oisis)  
  
# Never prompts the user for choices on installation/configuration of packages  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM linux  
# Work around initramfs-tools running on kernel 'upgrade':
<http://bugs.debian.org/cgi-bin/bugreport.cgi?bug=594189>  
ENV INITRD No  
  
RUN echo "deb http://ftp.debian.org/debian jessie-backports main" >
/etc/apt/sources.list.d/backports.list  
  
RUN apt-get update \  
&& apt-get install -yqq collectd -t jessie-backports \  
&& apt-get install -yqq \  
supervisor python-pip \  
&& pip install envtpl \  
&& apt-get clean \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base  
  
RUN mkdir -p /etc/collectd/plugins.conf.d  
COPY plugins-conf /etc/collectd/plugins.conf.d  
COPY config/collectd.conf.tpl /etc/collectd/collectd.conf.tpl  
COPY config/write_graphite.conf.tpl
/etc/collectd/collectd.conf.d/write_graphite.conf.tpl  
COPY config/write_influxdb.conf.tpl
/etc/collectd/collectd.conf.d/write_influxdb.conf.tpl  
COPY config/write_logstash.conf.tpl
/etc/collectd/collectd.conf.d/write_logstash.conf.tpl  
COPY config/tsdb.conf.tpl /etc/collectd/collectd.conf.d/tsdb.conf.tpl  
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY scripts/run.sh /root/run.sh  
RUN chmod +x /root/run.sh  
  
ENTRYPOINT ["/root/run.sh"]  

