FROM centos:7  
  
RUN yum -y install deltarpm wget \  
&& yum -y update \  
&& yum -y install epel-release \  
&& yum -y install supervisor \  
&& wget -qO /usr/bin/dumb-init https://github.com/Yelp/dumb-
init/releases/download/v1.0.3/dumb-init_1.0.3_amd64 \  
&& chmod +x /usr/bin/dumb-init \  
&& yum -y remove deltarpm epel-release wget \  
&& yum clean all \  
&& rm -rf /var/cache/yum \  
&& mkdir -p /config/{supervisor,init}  
  
COPY container-files/* /tmp/  
  
RUN mv /tmp/watcher.sh /usr/bin/watcher.sh \  
&& mv /tmp/watcher.ini /config/supervisor/watcher.ini \  
&& mv /tmp/supervisor.ini /config/supervisor.ini \  
&& mv /tmp/placeholder.sh /config/init/placeholder.sh \  
&& mv /tmp/entry.sh /entry.sh  
  
CMD [ "/entry.sh" ]  

