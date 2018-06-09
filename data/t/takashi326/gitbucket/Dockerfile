FROM java:8-jre  
  
MAINTAINER takashi326  
  
ADD
https://github.com/gitbucket/gitbucket/releases/download/4.10/gitbucket.war
/opt/gitbucket.war  
  
RUN ln -s /gitbucket /root/.gitbucket  
  
VOLUME /gitbucket  
  
EXPOSE 8080  
CMD ["java", "-jar", "/opt/gitbucket.war"]  

