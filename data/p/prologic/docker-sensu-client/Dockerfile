FROM hiroakis/docker-sensu-server  
  
ENTRYPOINT ["/opt/run-sensu-client.sh"]  
  
RUN yum install -y nc  
  
ADD supervisor.conf /etc/supervisord.conf  
ADD config.json /tmp/sensu/config.json  
ADD client.json /tmp/sensu/conf.d/client.json  
ADD run-sensu-client.sh /opt/run-sensu-client.sh  
RUN chmod 700 /opt/run-sensu-client.sh  

