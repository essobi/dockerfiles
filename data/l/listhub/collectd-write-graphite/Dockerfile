FROM ubuntu  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -y update  
RUN apt-get -y install collectd collectd-utils curl python-pip  
  
# add a fake mtab for host disk stats  
ADD etc_mtab /etc/mtab  
  
ADD collectd.conf.tpl /etc/collectd/collectd.conf.tpl  
  
ADD local_settings.py /opt/graphite/webapp/graphite/local_settings.py  
  
RUN pip install envtpl  
ADD start_container /usr/bin/start_container  
RUN chmod +x /usr/bin/start_container  
CMD start_container  

