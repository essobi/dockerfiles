FROM cyberluisda/kafka-connect:0.11.0.0  
  
MAINTAINER Luis David Barrios Alfonso (cyberluisda@gmail.com)  
  
# Install ivy  
ENV IVI_VERSION 2.4.0  
  
RUN cd /usr/lib && \  
curl "http://ftp.cixug.es/apache/ant/ivy/${IVI_VERSION}/apache-
ivy-${IVI_VERSION}-bin-with-deps.tar.gz" | tar -zxvf - && \  
rm -fr /usr/lib/apache-ivy-${IVI_VERSION}/src /usr/lib/apache-
ivy-${IVI_VERSION}/doc  
RUN mkdir -p /usr/share/java/ && ln -s /usr/lib/apache-
ivy-${IVI_VERSION}/ivy-2.4.0.jar /usr/share/java/ivy.jar  
# Download kafka connect libs and add to classpath  
RUN mkdir -p /usr/lib/kafka/connect-es  
COPY files/ivy.xml /usr/lib/kafka/connect-es/  
COPY files/ivy-settings.xml /usr/lib/kafka/connect-es/  
RUN java \  
-jar /usr/share/java/ivy.jar \  
-settings /usr/lib/kafka/connect-es/ivy-settings.xml \  
-ivy /usr/lib/kafka/connect-es/ivy.xml \  
-retrieve "/usr/lib/kafka/connect-es/[artifact]-[revision].[ext]"  
# Remove conflicts  
RUN rm -f \  
/usr/lib/kafka/connect-es/guava-18.0.jar  
ENV CLASSPATH $CLASSPATH:/usr/lib/kafka/connect-es/*  

