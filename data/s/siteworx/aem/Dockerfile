FROM java:openjdk-7u79-jdk  
  
RUN mkdir /opt/aem/  
  
WORKDIR /opt/aem/  
  
COPY cq-quickstart-5.6.1.jar /opt/aem/cq-quickstart-5.6.1.jar  
COPY license.properties /opt/aem/license.properties  
  
RUN java -jar cq-quickstart-5.6.1.jar -unpack -v  
  
EXPOSE 4502  
ENV CQ_FOREGROUND y  
ENV CQ_VERBOSE y  
ENV CQ_NOBROWSER y  
ENV CQ_RUNMODE "dev,author,nosamplecontent"  
ENV CQ_JVM_OPTS "-server -Xmx1524M -Xms512M -XX:MaxPermSize=512M"  
RUN apt-get update  
RUN apt-cache search maven  
RUN apt-get -y install maven  
RUN mvn -version  
  
RUN apt-get -y install tmux  
  
CMD crx-quickstart/bin/quickstart  

