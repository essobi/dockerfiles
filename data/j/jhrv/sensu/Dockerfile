FROM centos:6  
MAINTAINER Johnny Horvi <johnny.horvi@gmail.com>  
  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/i386/epel-
release-6-8.noarch.rpm  
RUN rpm --import http://www.rabbitmq.com/rabbitmq-signing-key-public.asc  
COPY sensu.repo /etc/yum.repos.d/  
  
RUN yum install -y erlang \  
rabbitmq-server \  
redis \  
sensu \  
supervisor  
  
RUN echo "EMBEDDED_RUBY=true" > /etc/default/sensu & ln -s
/opt/sensu/embedded/bin/ruby /usr/bin/ruby  
RUN /opt/sensu/embedded/bin/gem install influxdb  
  
COPY influx.rb /etc/sensu/extensions/  
COPY run.sh /opt/  
COPY supervisord.conf /etc/  
  
VOLUME /etc/sensu  
VOLUME /var/log/sensu  
  
# sensu-api  
EXPOSE 4567  
# rabbitmq  
EXPOSE 5672  
CMD ["/opt/run.sh"]  

