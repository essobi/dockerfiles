FROM google/debian:wheezy  
MAINTAINER Jordan Li  
RUN apt-get update -y && apt-get install --no-install-recommends -y -q curl
python build-essential git ca-certificates openjdk-7-jre  
RUN mkdir /nodejs && curl
https://nodejs.org/dist/v0.12.7/node-v0.12.7-linux-x64.tar.gz | tar xvzf - -C
/nodejs --strip-components=1  
RUN curl -s http://archive.apache.org/dist/storm/apache-storm-0.9.5/apache-
storm-0.9.5.tar.gz | \  
tar zxf - -C /opt && \  
mv /opt/apache-storm-0.9.5 /opt/apache-storm  
ENV PATH $PATH:/nodejs/bin  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
ADD configure.sh /  
  

