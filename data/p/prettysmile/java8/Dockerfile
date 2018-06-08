FROM ubuntu  
  
ENV JAVA_HOME /java  
  
RUN apt-get update \  
&& apt-get -y install tar wget \  
&& wget
https://artifacts.alfresco.com/nexus/content/repositories/thirdparty/com/oracle/java/jre/1.8.0_65/jre-1.8.0_65-linux.tgz
\  
&& tar -zxvf jre-1.8.0_65-linux.tgz \  
&& rm jre-1.8.0_65-linux.tgz

