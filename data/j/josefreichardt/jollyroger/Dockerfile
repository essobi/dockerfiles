FROM josefreichardt/jollyroger:parent-latest  
  
# Add sources  
ADD https://bitbucket.org/Josef-Reichardt/jollyroger/downloads/jollyroger-
budget-latest.jar /opt/jollyroger-budget/jollyroger-budget-latest.jar  
WORKDIR /opt/jollyroger-budget  
  
# start  
ENV JAVA_OPTS=""  
ENTRYPOINT [ "sh", "-c", "java $JAVA_OPTS
-Djava.security.egd=file:/dev/./urandom -jar jollyroger-budget-latest.jar
--spring.profiles.active=prod" ]  
EXPOSE 8080  

