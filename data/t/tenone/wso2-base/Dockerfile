FROM ubuntu:15.10  
MAINTAINER Max Cai <max@hubub.com>  
  
# Install Java.  
RUN \  
apt-get update && \  
apt-get install -y software-properties-common && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN apt-get update && apt-get install -y wget unzip curl  
  
  
ENV JAVA_HOME=/usr/lib/jvm/java-8-oracle/  
ENV WSO2_HOME /svc  
WORKDIR ${WSO2_HOME}  
  
EXPOSE 9443 9763 8280 8243  
RUN curl 'http://product-dist.wso2.com/products/api-
manager/1.10.0/wso2am-1.10.0.zip' -H 'Connection: keep-alive' \--compressed -o
wso2am.zip  
  
RUN unzip wso2am.zip -d wso2am && mv wso2am/*/* wso2am && rm wso2am.zip  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

