FROM maven:3-jdk-8  
WORKDIR /opt  
  
RUN git clone \--depth 1 -b 1.4.1 https://github.com/apache/ignite.git \  
&& cd ignite \  
&& mvn clean package -DskipTests  
  
WORKDIR /opt/ignite  
  
CMD ./bin/ignite.sh  

