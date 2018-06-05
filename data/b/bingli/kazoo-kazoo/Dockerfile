FROM bingli/kazoo-base  
MAINTAINER Bing Li <bingli1000@gmail.com>  
  
RUN yum install -y kazoo-R15B  
  
ADD entrypoint.sh init.sh /root/  
  
VOLUME ["/var/lib/rabbitmq", "/opt/kazoo/log", "/var/log/2600hz",
"/var/www/html"]  
  
ENTRYPOINT ["/root/entrypoint.sh"]  
  

