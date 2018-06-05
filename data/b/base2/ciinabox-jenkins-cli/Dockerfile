FROM develar/java  
  
MAINTAINER "Aaron Walker" <aaronpwalker@gmail.com>  
  
ADD jenkins-cli.jar /opt/jenkins/jenkins-cli.jar  
WORKDIR /opt/jenkins  
  
ENTRYPOINT ["java", "-jar", "jenkins-cli.jar", "-noCertificateCheck",
"-noKeyAuth"]  
  
CMD ["--help"]  

