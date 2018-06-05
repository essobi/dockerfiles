FROM dockerfile/java  
MAINTAINER SequenceIQ  
  
RUN curl -Ls https://raw.githubusercontent.com/sequenceiq/ambari-
shell/master/latest-snap.sh | bash  
ADD install-cluster.sh /tmp/  
ADD wait-for-host-number.sh /tmp/  
WORKDIR /tmp  
  
ENTRYPOINT ["java", "-jar", "ambari-shell.jar"]  

