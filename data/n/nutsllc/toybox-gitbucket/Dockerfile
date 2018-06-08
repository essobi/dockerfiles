FROM java:8-jre-alpine  
MAINTAINER Nuts Project, LLC  
  
ADD https://github.com/gitbucket/gitbucket/releases/download/4.1/gitbucket.war
/opt/gitbucket.war  
RUN ln -s /gitbucket /root/.gitbucket  
  
VOLUME /gitbucket  
  
# for web page  
EXPOSE 8080  
# for SSH  
EXPOSE 29418  
ADD docker-entrypoint-ex.sh /entrypoint-ex.sh  
  
ENTRYPOINT ["/entrypoint-ex.sh"]  
CMD ["java", "-jar", "/opt/gitbucket.war"]  

