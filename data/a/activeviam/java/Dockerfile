FROM ubuntu:16.04  
  
RUN apt-get update && \  
apt-get install -y debconf-utils software-properties-common python-software-
properties && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
bash -c 'echo "oracle-java8-installer shared/accepted-oracle-license-v1-1
select true" | debconf-set-selections' && \  
apt-get install -y oracle-java8-installer && \  
apt-get clean -y  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV JRE_HOME /usr/lib/jvm/java-8-oracle/jre  
ENV PATH "${PATH}:${JAVA_HOME}/bin:${JAVA_HOME}/bin"  

