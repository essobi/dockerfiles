FROM centos:latest  
  
MAINTAINER Roman Pridybailo <roman.pridybailo@kruschecompany.com>  
  
RUN yum -y update && yum install -y wget python-devel mysql-devel gcc \  
&& wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
\  
&& rpm -i epel-release-latest-7.noarch.rpm && yum -y update \  
&& yum install -y python python-pip \  
&& /usr/bin/pip install -U pip \  
&& /usr/bin/pip install pyTelegramBotAPI watchdog MySQL-python j2cli
j2cli[yaml]

