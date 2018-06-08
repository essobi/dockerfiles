FROM dockerfile/java:oracle-java7  
MAINTAINER stuart nixon <stuart@rednut.net>  
  
WORKDIR /opt  
  
RUN \  
wget
'http://downloads.sourceforge.net/project/javagroups/JGroups/3.3.3.Final/jgroups-3.3.3.Final.jar'
-O /opt/jgroups-3.3.3.Final.jar  
  
ADD ./run-jgroups.sh /opt/run-jgroups.sh  
RUN chmod +x /opt/run-jgroups.sh  
  
EXPOSE 45566  
ENTRYPOINT [ "/opt/run-jgroups.sh" ]  
  

