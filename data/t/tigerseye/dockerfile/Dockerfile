FROM alpine:edge  
RUN apk add --no-cache git openssh-client curl unzip bash ttf-dejavu coreutils
ansible jenkins  
  
EXPOSE 8080  
VOLUME /var/jenkins_home  
CMD ["java", "-jar", "/usr/share/webapps/jenkins/jenkins.war"]  

