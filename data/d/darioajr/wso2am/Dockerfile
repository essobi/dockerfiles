FROM java:7  
MAINTAINER Dario Alves Junior, darioajr@gmail.com  
  
RUN wget -P /opt https://github.com/wso2/product-
apim/releases/download/v1.9.1/wso2am-1.9.1.zip && \  
apt-get update && \  
apt-get install -y zip && \  
apt-get clean && \  
unzip /opt/wso2am-1.9.1.zip -d /opt && \  
rm /opt/wso2am-1.9.1.zip  
  
ENV JAVA_HOME /usr/lib/jvm/java-7-openjdk-amd64  
EXPOSE 9443  
CMD ["/opt/wso2am-1.9.1/bin/wso2server.sh"]

