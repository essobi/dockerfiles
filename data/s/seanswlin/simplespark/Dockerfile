FROM ubuntu:14.04  
RUN apt-get install -y software-properties-common  
RUN apt-add-repository ppa:webupd8team/java  
RUN apt-get update  
RUN apt-get install -y openjdk-7-jre-headless  
RUN apt-get install -y wget  
RUN wget http://d3kbcqa49mib13.cloudfront.net/spark-1.6.0-bin-hadoop2.4.tgz  
RUN tar xvf spark-1.6.0-bin-hadoop2.4.tgz -C /opt  
RUN rm spark-1.6.0-bin-hadoop2.4.tgz  
RUN mv /opt/spark-1.6.0-bin-hadoop2.4 /opt/spark  
  

