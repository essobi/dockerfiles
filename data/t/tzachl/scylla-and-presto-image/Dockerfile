# Add monitoring agent to Scylla Docker image  
FROM scylladb/scylla  
MAINTAINER Tzach Livyatan  
  
#install presto  
RUN yum install wget gunzip tar less -y  
RUN wget https://repo1.maven.org/maven2/com/facebook/presto/presto-
server/0.152/presto-server-0.152.tar.gz  
RUN gunzip presto-server-0.152.tar.gz  
RUN tar -xvf presto-server-0.152.tar  
RUN mv presto-server-0.152 presto-server  
RUN rm presto-server-0.152.tar  
  
ADD presto-etc presto-server/etc  
ADD supervisor/ /etc/supervisord.conf.d  
ADD presto.sh presto.sh  
  
# install Presto CLI  
RUN wget https://repo1.maven.org/maven2/com/facebook/presto/presto-
cli/0.152/presto-cli-0.152-executable.jar  
RUN mv presto-cli-0.152-executable.jar presto  
RUN chmod a+x presto  
  

