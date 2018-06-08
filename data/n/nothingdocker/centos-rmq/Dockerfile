# Version 1.0.0  
FROM nothingdocker/centos-nodex  
COPY ./rabbitmq.config /etc/rabbitmq/rabbitmq.config  
RUN wget https://github.com/rabbitmq/rabbitmq-
server/releases/download/rabbitmq_v3_6_9/rabbitmq-
server-3.6.9-1.el7.noarch.rpm;\  
rpm --import https://www.rabbitmq.com/rabbitmq-release-signing-key.asc;\  
yum -y install rabbitmq-server-3.6.9-1.el7.noarch.rpm;\  
yum clean all;\  
rm -f rabbitmq-server-3.6.9-1.el7.noarch.rpm;\  
systemctl enable rabbitmq-server;\  
rabbitmq-plugins enable rabbitmq_management;  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/sbin/init"]  

