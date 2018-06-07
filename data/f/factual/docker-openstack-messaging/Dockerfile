FROM factual/docker-base  
MAINTAINER Maxime DEVALLAND <maxime@factual.com>  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 5EDB1B62EC4926EA  
RUN echo "deb http://ubuntu-cloud.archive.canonical.com/ubuntu trusty-
updates/kilo main" > /etc/apt/sources.list.d/cloudarchive-kilo.list  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
--force-yes ntp ubuntu-cloud-keyring rabbitmq-server && rm -r
/var/lib/apt/lists/*  
RUN /usr/sbin/rabbitmq-server &  
RUN mkdir -p /etc/my_init.d/ /etc/service/rabbitmq  
ADD create_user.sh /etc/my_init.d/z_create_user.sh  
ADD rabbitmq.sh /etc/service/rabbitmq/run  
  
EXPOSE 5672  
RUN netstat -antp  

