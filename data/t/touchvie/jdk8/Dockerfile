from ubuntu:xenial  
  
ENV LANG C.UTF-8  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Install dependencies  
RUN apt-get update && apt-get install -y git build-essential curl wget
software-properties-common  
  
# Install JDK 8  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer wget unzip tar && \  
rm -rf /var/cache/oracle-jdk8-installer && \  
apt-get install -y oracle-java8-set-default

