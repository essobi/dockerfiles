FROM java:7  
MAINTAINER Teerat Pitakrat  
  
WORKDIR /opt/recipes-rss/  
ADD https://github.com/hora-prediction/recipes-rss-
kube/releases/download/0.3/rss-edge-0.3.jar /opt/recipes-rss/rss-edge.jar  
EXPOSE 9090  
CMD ["java", "-jar", "rss-edge.jar"]  

