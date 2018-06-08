FROM ubuntu:14.04  
MAINTAINER Mark Ng <mng@liquidweb.com>  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y git vim curl
python-pip libpython-dev libssl-dev libffi-dev && apt-get clean  
RUN curl -LO
https://github.com/coreos/etcd/releases/download/v2.1.0-alpha.0/etcd-v2.1.0-alpha.0-linux-
amd64.tar.gz  
RUN tar xzvf etcd-v2.1.0-alpha.0-linux-amd64.tar.gz  
RUN cd etcd-v2.1.0-alpha.0-linux-amd64 && cp etcdctl /usr/local/bin  
  
ADD requirements.txt requirements.txt  
RUN pip install --upgrade pip  
RUN pip install -r requirements.txt  
  
RUN /bin/bash  

