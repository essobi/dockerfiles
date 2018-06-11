FROM centos:centos6  
MAINTAINER Utsav Kumar <utsav2307@gmail.com>  
RUN yum install -y epel-release && \  
yum install -y ansible && \  
echo "localhost ansible_connection=local" >> /etc/ansible/hosts && \  
yum install -y git  
CMD "echo Container launched"  

