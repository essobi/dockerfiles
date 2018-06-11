FROM java:8-jdk  
  
MAINTAINER Aaron Zirbes <aaron@zirbes.org>  
  
ENV LKT_ORG=com/mnclimbingcoop \  
LKT_BINTRAY_REPO=mnclimbingcoop/maven \  
LKT_VERSION=0.8.9  
RUN mkdir -p /usr/local/lakitu  
ADD
https://bintray.com/artifact/download/${LKT_BINTRAY_REPO}/${LKT_ORG}/lakitu/${LKT_VERSION}/lakitu-${LKT_VERSION}.jar
/usr/local/lakitu/lakitu.jar  
ADD start.sh /usr/local/lakitu/  
RUN chmod 0755 /usr/local/lakitu/start.sh  
RUN mkdir -p /usr/local/lakitu/config  
ADD application.properties /usr/local/lakitu/config/application.properties  
RUN ln -s /usr/local/lakitu/config/application.properties  
  
WORKDIR /usr/local/lakitu  
  
EXPOSE 8080 8181  
ENTRYPOINT ["/usr/local/lakitu/start.sh"]  

