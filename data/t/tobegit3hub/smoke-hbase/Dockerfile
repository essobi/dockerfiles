FROM ubuntu:14.04  
MAINTAINER tobe tobeg3oogle@gmail.com  
  
RUN apt-get update  
  
# Install Oracle Java7  
RUN apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get install -y oracle-java7-installer  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle/  
  
# Install tools  
RUN apt-get install -y maven  
  
# Install smoke-hbase  
ADD . /smoke-hbase  
WORKDIR /smoke-hbase  
RUN mvn clean package -DskipTests  
  
CMD ["bash", "target/smoke-hbase-1.0.0-SNAPSHOT/bin/smoke-hbase.sh"]

