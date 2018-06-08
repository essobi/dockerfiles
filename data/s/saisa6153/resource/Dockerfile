FROM centos:centos6  
MAINTAINER saisa6153  
  
USER root  
WORKDIR /opt  
  
# yum  
RUN yum install -y http://linux.mirrors.es.net/fedora-
epel/6Server/x86_64/epel-release-6-8.noarch.rpm  
RUN yum update -y  
RUN yum --nogpgcheck install -y passwd sudo gcc gcc-c++ make git openssl-devel
zlib-devel bzip2 bzip2-devel libevent-devel openssh openssh-server readline-
devel tar expat-devel ntp mysql-server hostname python-pip
java-1.7.0-openjdk.x86_64 wget  
RUN yum clean all  
  
# supervisor  
RUN /usr/bin/pip install supervisor  
ADD supervisord.conf /etc/  
  
# mysql Port 3306  
RUN mv /etc/my.cnf ~  
ADD my.cnf /etc/  
RUN /usr/bin/mysql_install_db --user=mysql --datadir=/var/lib/mysql  
  
# DynamoDB local Port 8000  
RUN wget http://dynamodb-local.s3-website-us-
west-2.amazonaws.com/dynamodb_local_latest -O dynamo.tar.gz  
RUN mkdir dynamodb_local  
RUN tar xvzf dynamo.tar.gz -C /opt/dynamodb_local && rm -f dynamo.tar.gz  
  
# ElasticMQ Port 9324  
RUN wget https://s3-eu-west-1.amazonaws.com/softwaremill-public/elasticmq-
server-0.8.2.jar -O elasticmq.jar  
ADD elasticmq.conf /etc/  
  
EXPOSE 8000 9324 3306  
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]

