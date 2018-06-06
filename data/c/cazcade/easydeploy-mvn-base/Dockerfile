FROM ubuntu:14.04  
MAINTAINER <neil@cazcade.com>  
RUN sed -i.bak 's/main$/main universe/' /etc/apt/sources.list  
RUN apt-get update  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN apt-get update  
RUN apt-get -y install build-essential python-software-properties software-
properties-common wget curl  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get -y install oracle-java8-installer && apt-get clean  
RUN update-alternatives --display java  
RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/environment  
RUN apt-get install -y maven wget  
RUN echo deb http://apt.newrelic.com/debian/ newrelic non-free >>
/etc/apt/sources.list.d/newrelic.list  
RUN wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add -  
RUN apt-get -qq update  
RUN apt-get install newrelic-sysmond  
  

