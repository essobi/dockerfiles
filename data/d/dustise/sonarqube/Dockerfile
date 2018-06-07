FROM dustise/oracle-jdk:latest  
ENV SONAR_VERSION=6.2 \  
SONARQUBE_HOME=/usr/share/sonarqube \  
# Database configuration  
# Defaults to using H2  
SONARQUBE_JDBC_USERNAME=sonar \  
SONARQUBE_JDBC_PASSWORD=sonar \  
SONARQUBE_JDBC_URL=  
  
COPY run.sh /usr/local/bin/  
COPY prepare.sh /usr/local/bin  
RUN /usr/local/bin/prepare.sh  
  
# Http port  
EXPOSE 9000  
VOLUME ["$SONARQUBE_HOME/data", "$SONARQUBE_HOME/extensions",
"$SONARQUBE_HOME/conf"]  
CMD ["run.sh"]  

