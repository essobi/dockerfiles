FROM java:7  
MAINTAINER Teerat Pitakrat  
  
WORKDIR /opt/recipes-rss/  
ADD https://github.com/hora-prediction/recipes-rss-
kube/releases/download/0.3/rss-middletier-0.3.jar /opt/recipes-rss/rss-
middletier.jar  
EXPOSE 9191  
CMD ["java", "-jar", "rss-middletier.jar"]  

