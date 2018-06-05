FROM ubuntu:14.04  
MAINTAINER Michele Cantelli <emmekappa@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive  
RUN apt-get -y update  
RUN apt-get install -y --force-yes software-properties-common  
RUN apt-add-repository -y ppa:webupd8team/java  
RUN apt-get -y update  
RUN /bin/echo debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
RUN apt-get -y install oracle-java7-installer oracle-java7-set-default  
  
RUN apt-get -y install curl nano telnet htop  
RUN curl -s http://d3kbcqa49mib13.cloudfront.net/spark-1.5.2-bin-hadoop2.4.tgz
| tar -xz -C /usr/local/  
RUN cd /usr/local && ln -s spark-1.5.2-bin-hadoop2.4 spark  
ADD scripts/start-master.sh /start-master.sh  
ADD scripts/start-worker.sh /start-worker.sh  
ADD scripts/spark-shell.sh /spark-shell.sh  
ADD scripts/remove_alias.sh /remove_alias.sh  
ADD scripts/spark-env.sh /spark-env.sh  
ADD scripts/spark-defaults.conf /spark-defaults.conf  
ENV SPARK_HOME /usr/local/spark  
  
EXPOSE 8080 7077  
#8888 8081 4040 7001 7002 7003 7004 7005 7006  

