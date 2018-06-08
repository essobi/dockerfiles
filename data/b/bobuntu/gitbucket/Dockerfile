FROM openjdk:8-jre-alpine  
  
ADD
https://github.com/gitbucket/gitbucket/releases/download/4.11/gitbucket.war
/opt/gitbucket.war  
  
RUN apk add --no-cache bash expect && \  
ln -s /gitbucket /root/.gitbucket  
  
EXPOSE 8080 29418  
ADD entrypoint.sh /opt/  
  
CMD ["/opt/entrypoint.sh"]  

