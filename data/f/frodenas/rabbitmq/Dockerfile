FROM frodenas/ubuntu  
MAINTAINER Ferran Rodenas <frodenas@gmail.com>  
  
# Install RabbitMQ 3.3.4  
RUN DEBIAN_FRONTEND=noninteractive && \  
cd /tmp && \  
wget http://www.rabbitmq.com/rabbitmq-signing-key-public.asc && \  
apt-key add rabbitmq-signing-key-public.asc && \  
echo 'deb http://www.rabbitmq.com/debian/ testing main' >>
/etc/apt/sources.list.d/rabbitmq.list && \  
apt-get update && \  
apt-get install -y --force-yes rabbitmq-server && \  
rabbitmq-plugins enable rabbitmq_management && \  
service rabbitmq-server stop && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Add scripts  
ADD scripts /scripts  
RUN chmod +x /scripts/*.sh  
RUN touch /.firstrun  
  
# Command to run  
ENTRYPOINT ["/scripts/run.sh"]  
CMD [""]  
  
# Expose listen port  
EXPOSE 5672  
EXPOSE 15672  
# Expose our log volumes  
VOLUME ["/var/log/rabbitmq"]  

