#################################################################  
# Creates a basic RabbitMQ image with the latest RabbitMQ version  
#  
# ## .  
# ## ## ## ==  
# ## ## ## ## ===  
# /""""""""""""""""\\___/ ===  
# ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ / ===- ~~~  
# \\______ o __/  
# \ \ __/  
# \\____\\______/  
#  
# Author: Kale Franz <kale@franz.io>  
# License: MIT  
#################################################################  
  
FROM kalefranz/centos:latest  
MAINTAINER Kale Franz <kale@franz.io>  
  
# import rabbitmq signing key  
RUN rpm --import http://www.rabbitmq.com/rabbitmq-signing-key-public.asc  
  
# figure out latest version number of rabbitmq, then download it  
RUN /usr/bin/curl -s 'http://www.rabbitmq.com/releases/rabbitmq-
server/current/' | gawk 'match($0, /<a href="rabbitmq-
server-([-.0-9]*).noarch.rpm">/, ary) {print ary[1]}' | { read
RABBITMQ_LATEST; /usr/bin/wget -O rabbitmq-server.noarch.rpm
http://www.rabbitmq.com/releases/rabbitmq-server/current/rabbitmq-
server-${RABBITMQ_LATEST}.noarch.rpm; }  
  
RUN yum -y install rabbitmq-server.noarch.rpm  
RUN rm -rf rabbitmq-server.noarch.rpm  
  
# start rabbitmq-server daemon on boot  
RUN /sbin/chkconfig rabbitmq-server on  
  
# enable management plugin -- default port 15672  
RUN /usr/sbin/rabbitmq-plugins enable rabbitmq_management  
RUN /sbin/service rabbitmq-server restart  
  
EXPOSE 5672 15672  
  
CMD ["/usr/sbin/rabbitmq-server"]  

