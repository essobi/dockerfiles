FROM ubuntu:14.04  
MAINTAINER Fu Cheng <alexcheng1982@gmail.com>  
  
# Install dependencies  
RUN apt-get update  
RUN apt-get -y install unzip curl openjdk-7-jre-headless  
RUN cd /tmp && curl -L -O http://dist.sonar.codehaus.org/sonarqube-4.4.zip &&
unzip sonarqube-4.4.zip && mv sonarqube-4.4 /opt/sonar  
  
# Update SonarQube configuration  
RUN sed -i
's|#wrapper.java.additional.7=-server|wrapper.java.additional.7=-server|g'
/opt/sonar/conf/wrapper.conf  
RUN sed -i
's|sonar.jdbc.username=sonar|sonar.jdbc.username=${env:DB_USERNAME}|g'
/opt/sonar/conf/sonar.properties  
RUN sed -i
's|sonar.jdbc.password=sonar|sonar.jdbc.password=${env:DB_PASSWORD}|g'
/opt/sonar/conf/sonar.properties  
RUN sed -i 's|sonar.jdbc.url=jdbc:h2|#sonar.jdbc.url=jdbc:h2|g'
/opt/sonar/conf/sonar.properties  
RUN sed -i
's|#sonar.jdbc.url=jdbc:mysql://localhost|sonar.jdbc.url=jdbc:mysql://${env:DB_URL}|g'
/opt/sonar/conf/sonar.properties  
  
EXPOSE 9000  
CMD ["/opt/sonar/bin/linux-x86-64/sonar.sh","console"]  
  

