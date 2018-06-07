FROM ubuntu:precise  
  
RUN apt-get update  
RUN apt-get install -yq wget  
  
RUN wget -O /etc/apt/sources.list.d/cloudera.list
http://archive.cloudera.com/impala/ubuntu/precise/amd64/impala/cloudera.list  
RUN apt-key adv --recv-key --keyserver keyserver.ubuntu.com 327574EE02A818DD  
RUN apt-get update -o Dir::Etc::sourcelist="sources.list.d/cloudera.list" -o
Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0"  
RUN apt-get -yq install libsasl2-2 impala-shell  
  
ENTRYPOINT /usr/bin/impala-shell  

