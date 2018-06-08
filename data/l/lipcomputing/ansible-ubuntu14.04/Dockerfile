# docker build --rm -t ansible-ubuntu14.04 .  
FROM ubuntu:14.04  
MAINTAINER Mario David <mariojmdavid@gmail.com>  
LABEL description="Run ansible roles and playbooks"  
RUN apt-get -y update \  
&& apt-get install software-properties-common -y \  
&& apt-add-repository ppa:ansible/ansible \  
&& apt-get -y update \  
&& apt-get install -y ansible git python-pip vim wget \  
&& apt-get clean \  
&& echo "localhost ansible_connection=local" > /etc/ansible/hosts  

