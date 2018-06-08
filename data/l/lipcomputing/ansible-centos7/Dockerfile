# docker build --rm -t ansible-centos7 .  
FROM centos:7  
MAINTAINER Mario David <mariojmdavid@gmail.com>  
LABEL description="Run ansible roles and playbooks"  
  
RUN yum -y update \  
&& yum -y install epel-release \  
&& yum -y install ansible git python-pip vim wget \  
&& yum clean all \  
&& echo "localhost ansible_connection=local" > /etc/ansible/hosts  

