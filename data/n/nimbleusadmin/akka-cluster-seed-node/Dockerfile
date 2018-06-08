FROM ubuntu:14.04  
MAINTAINER Nimbleus, LLC  
RUN apt-get update  
RUN apt-get install -y -q software-properties-common python-software-
properties  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
RUN apt-get install -y curl  
RUN apt-get install -y unzip  
RUN apt-get install -y wget  
RUN apt-get install -y -q oracle-java8-installer  
RUN rm -rf /var/lib/apt/lists/*  
RUN rm -rf /var/cache/oracle-jdk8-installer  
RUN curl -L -o akka-cluster-seed-node-2.4.8.zip
-unimbleus:8540ad9b559fb5ae28775a4c0831751c0ef004bf
'https://dl.bintray.com/nimbleus/nacreous/akka-cluster-seed-node-2.4.8.zip'  
RUN mkdir /app  
RUN mv akka-cluster-seed-node-2.4.8.zip /app  
WORKDIR /app  
RUN unzip akka-cluster-seed-node-2.4.8.zip  
WORKDIR /app/akka-cluster-seed-node-2.4.8/bin  
RUN chmod +x /app/akka-cluster-seed-node-2.4.8/bin/akka-cluster-seed-node  
EXPOSE 9000  
ENTRYPOINT ["/app/akka-cluster-seed-node-2.4.8/bin/akka-cluster-seed-node"]  

