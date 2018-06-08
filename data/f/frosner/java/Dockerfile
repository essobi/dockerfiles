FROM phusion/baseimage:0.9.18  
  
MAINTAINER Frank Rosner <frank@fam-rosner.de>  
  
RUN apt-get install -y software-properties-common \  
&& add-apt-repository ppa:webupd8team/java \  
&& apt-get update \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| debconf-set-selections \  
&& apt-get install -y oracle-java8-installer \  
&& apt-get clean all -y  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  

