FROM openjdk:8u151-jre  
  
ENV PDIBRANCH=6.1  
ENV PDIVERSION=6.1.0.1-196  
RUN sh -c "cd /opt && curl -JLO
https://sourceforge.net/projects/pentaho/files/Data%20Integration/$PDIBRANCH/pdi-
ce-$PDIVERSION.zip/download"  
  
RUN unzip /opt/*.zip -d /opt  
  
RUN rm /opt/*.zip  
  
RUN curl -JLO "https://dev.mysql.com/get/Downloads/Connector-J/mysql-
connector-java-5.1.45.tar.gz"  
  
RUN tar -zxvf mysql-connector-java-5.1.45.tar.gz  
  
RUN cp mysql-connector-java-5.1.45/mysql-connector-java-5.1.45-bin.jar
/opt/data-integration/lib/  
  
RUN apt-get update && apt-get -y install jq  
  
RUN mkdir -p /root/.kettle

