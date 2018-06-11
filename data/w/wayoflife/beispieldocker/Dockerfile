FROM tomcat:7  
MAINTAINER "Daniel Betsche" <dbetsche@gmail.com>  
  
ADD http://mirrors.jenkins-ci.org/war/latest/jenkins.war
/usr/local/tomcat/webapp/  
  
ENTRYPOINT ["/bin/bash"]  
CMD ["catalina.sh", "run"]  
  
EXPOSE 8080  

