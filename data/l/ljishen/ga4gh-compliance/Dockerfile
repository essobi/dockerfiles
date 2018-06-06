# VERSION 1.0  
FROM ubuntu:latest  
  
MAINTAINER Jianshen Liu <jliu120@ucsc.edu>  
  
# See http://www.webupd8.org/2012/09/install-oracle-java-8-in-ubuntu-via-
ppa.html  
# Install Oracle Java 8  
RUN apt-get update \  
&& apt-get install -y software-properties-common \  
&& add-apt-repository ppa:webupd8team/java \  
&& apt-get update \  
&& echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true
| /usr/bin/debconf-set-selections \  
&& apt-get install -y \  
oracle-java8-installer \  
oracle-java8-set-default  
  
# Install other pre-requisite packages  
RUN apt-get install -y git curl unzip  
  
# Install Apache Maven  
WORKDIR /root  
RUN curl http://apache.claz.org/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz | tar xz  
ENV PATH /root/apache-maven-3.3.9/bin:$PATH  
  
# Install Compliance Suite  
RUN git clone https://github.com/ga4gh/compliance.git  
WORKDIR /root/compliance  
RUN mvn clean install \  
&& unzip -ou dist/target/ga4gh-ctk-cli.zip -d testdir  
  
# Clean Up  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR /root/compliance/testdir  
ENTRYPOINT ["./ctk"]  

