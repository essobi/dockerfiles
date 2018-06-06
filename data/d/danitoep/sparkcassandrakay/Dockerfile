FROM ubuntu:14.04  
MAINTAINER Daniel Eguia <dani921114@gmail.com>  
  
# install java  
RUN apt-get -y update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes software-
properties-common python-software-properties  
RUN apt-get install software-properties-common -y  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN apt-get install wget -y  
RUN /bin/echo debconf shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections  
RUN apt-get install oracle-java8-installer -y  
RUN apt-get update -y  
  
# make serve directory  
RUN mkdir -p /srv  
WORKDIR "/srv"  
  
# scala 2.11 required for cassandra spark connector  
RUN wget http://downloads.lightbend.com/scala/2.11.8/scala-2.11.8.deb  
RUN dpkg -i scala-2.11.8.deb  
  
# get spark  
RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-2.0.0-bin-hadoop2.7.tgz  
RUN tar -zxf spark-2.0.0-bin-hadoop2.7.tgz  
RUN mv spark-2.0.0-bin-hadoop2.7 spark  
  
# build spark cassandra connector  
RUN echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a
/etc/apt/sources.list.d/sbt.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823  
RUN apt-get install apt-transport-https -y  
RUN apt-get update -y  
RUN apt-get install sbt -y  
RUN git clone https://github.com/datastax/spark-cassandra-connector.git  
RUN cd spark-cassandra-connector && git checkout master  
RUN cd spark-cassandra-connector && sbt assembly -Dscala-2.11=true  
  
# move spark cassandra connector to spark jar directory  
RUN find . -iname "*.jar" -type f -exec /bin/cp {} /srv/spark/jars/ \;  
  
WORKDIR /  
ADD scripts/start-spark.sh /start-spark.sh  
ADD scripts/spark-shell.sh /spark-shell.sh  
  
ADD spark-cassandra-connector-2.0.6-s_2.11.jar /srv/spark/jars/  
  
EXPOSE 8080 7077 8888 8081 4040 7001 7002 7003 7004 7005 7006  

