FROM azul/zulu-openjdk-debian  
MAINTAINER Ryan J. McDonough "ryan@damnhandy.com"  
ENV GITBUCKET_SHA 6920bae2e4fe7570d5831c5da5147feb  
  
ADD
https://github.com/gitbucket/gitbucket/releases/download/3.12/gitbucket.war
/opt/app/gitbucket.war  
  
VOLUME /var/gitbucket  
  
ENV GITBUCKET_HOME /var/gitbucket  
  
ENTRYPOINT ["java", "-jar", "/opt/app/gitbucket.war"]  
EXPOSE 8080  

