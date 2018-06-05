FROM openjdk:8u141-jre  
  
ADD https://github.com/dcos-utilities/f5-marathon-
autoscale/releases/download/1.0.0/f5-marathon-autoscale.jar /  
ADD tools/startup.sh /startup.sh  
RUN chmod +x /startup.sh  
  
ENTRYPOINT ["/startup.sh"]

