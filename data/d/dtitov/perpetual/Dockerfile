FROM ubuntu:17.04  
RUN apt update && apt install wget curl nano mc git openjdk-8-jdk maven -yq
--no-install-recommends  
ADD http://mirrors.jenkins.io/war/latest/jenkins.war jenkins.war  
EXPOSE 80  
ENTRYPOINT ["java", "-jar", "jenkins.war", "--httpPort=80"]  

