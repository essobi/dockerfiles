FROM java:jre  
  
MAINTAINER prince (https://github.com/prince-0203)  
  
ADD https://github.com/gitbucket/gitbucket/releases/download/4.2/gitbucket.war
/opt/gitbucket.war  
  
RUN ln -s /gitbucket /root/.gitbucket  
  
VOLUME /gitbucket  
  
# Port for web page  
EXPOSE 8080  
# Port for SSH access to git repository (Optional)  
EXPOSE 29418  
CMD ["java", "-jar", "/opt/gitbucket.war"]  

