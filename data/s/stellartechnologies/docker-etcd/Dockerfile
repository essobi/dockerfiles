FROM ubuntu:latest  
MAINTAINER Andy Kirkham <andy@spiders-lair.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y software-properties-common apt-transport-https \  
&& apt-get update \  
&& apt-get install -y python-pip curl wget  
RUN curl -sSL
https://github.com/coreos/etcd/releases/download/v2.2.0/etcd-v2.2.0-linux-
amd64.tar.gz | tar -C /usr/local -xz \  
&& ln -s /usr/local/etcd-v2.2.0-linux-amd64/etcd /usr/local/bin/etcd \  
&& ln -s /usr/local/etcd-v2.2.0-linux-amd64/etcdctl /usr/local/bin/etcdctl  
  
RUN apt-get -y clean && apt-get -y autoclean  
  
RUN mkdir /var/etcd/  
RUN mkdir /var/log/etcd/  
ADD aws.sh /aws.sh  
RUN chmod 755 /aws.sh  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
  
EXPOSE 4001 7001 2379 2380  
ENTRYPOINT ["/run.sh"]  
  

