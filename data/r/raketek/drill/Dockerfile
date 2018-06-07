FROM nimmis/java-centos:openjdk-7-jdk  
RUN wget http://apache.mirrors.hoobly.com/drill/drill-1.8.0/apache-
drill-1.8.0.tar.gz && tar -xzvf apache-drill-1.8.0.tar.gz && rm -rf apache-
drill-1.8.0.tar.gz  
  
# Set environment  
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk-1.7.0.111-2.6.7.2.el7_2.x86_64  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
EXPOSE 8047 31010 31011 31012  
ADD rundrill.sh rundrill.sh  
  
RUN chmod +x rundrill.sh  
  
ENTRYPOINT ["/root/rundrill.sh"]  

