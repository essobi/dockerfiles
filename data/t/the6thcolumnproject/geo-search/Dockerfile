#**************************************************************************  
# Copyright (c) 2012, The 6Th Column Project, LLC. *  
# Written by: The codewrx.org development team .et al *  
# *  
# All rights reserved. This file is part of the: *  
# The 6th Column Project, LLC / CodeWRX Software Stack *  
# *  
#**************************************************************************  
# Creates an Ubuntu 14 based image for Search *  
# *  
# ## . *  
# ## ## ## == *  
# ## ## ## ## === *  
# /""""""""""""""""\\___/ === *  
# ~~~ {~~ ~~~~ ~~~ ~~~~ ~~ ~ / ===- ~~~ *  
# \\______ o __/ *  
# \ \ __/ *  
# \\____\\______/ *  
# *  
#**************************************************************************  
# *  
# For details, see http://6thcolumn.org/ *  
# Please also read this link *  
# http://6thcolumn.org/LICENSE *  
# *  
#**************************************************************************  
FROM ubuntu:14.04  
#tell debian based distros to forget about user input  
ENV DEBIAN_FRONTEND noninteractive  
  
#update the de distro and install some basic tools  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y curl git vim emacs  
  
#Install java (curl command will certainly break if oracle changes his
download policy)  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN curl -L -C - -b "oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-pub/java/jdk/7u67-b01/jdk-7u67-linux-x64.tar.gz
>jdk-7u67-linux-x64.tar.gz  
RUN mkdir -p /opt/java && \  
cd /opt/java && \  
tar xzvf /jdk-7u67-linux-x64.tar.gz && \  
rm /jdk-7u67-linux-x64.tar.gz  
ENV PATH /opt/java/jdk1.7.0_67/bin:$PATH  
ENV JAVA_HOME /opt/java/jdk1.7.0_67  
  
#install elasticsearch  
RUN curl
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.1.tar.gz
| tar xzv  
RUN mv /elasticsearch-1.4.1 /elasticsearch  
  
#install elasticsearch plugins...  
RUN /elasticsearch/bin/plugin -install mobz/elasticsearch-head  
RUN /elasticsearch/bin/plugin -install polyfractal/elasticsearch-inquisitor  
  
#experimenting with xinet.d  
RUN apt-get -y install xinetd && \  
echo "container\t10101/tcp" >>/etc/services  
  
ADD xinetd.d/container /etc/xinetd.d/container  
ADD container/controller /container/controller  
ADD container/controller.d/start /container/controller.d/start  
ADD container/controller.d/stop /container/controller.d/stop  
ADD container/boot /container/boot  
  
#ENV CONTAINER_DATA /container_data  
#9200 elastic search  
#9300 elastic search  
#10101 container controller  
EXPOSE 9200 9300 10101  
#setting up the node  
ENV CONF_DIR /config # not working wihtout the initd script, cannot find it..  

