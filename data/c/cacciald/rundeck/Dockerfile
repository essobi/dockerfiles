FROM java:8-jre  
  
RUN useradd --home /opt/rundeck --shell /bin/bash rundeck  
  
WORKDIR /opt/rundeck  
  
ADD http://dl.bintray.com/rundeck/rundeck-maven/rundeck-launcher-2.7.2.jar
/opt/rundeck/rundeck.jar  
  
ADD https://github.com/rundeck/rundeck-cli/releases/download/v1.0.7/rundeck-
cli-1.0.7-all.jar /opt/rundeck/cli.jar  
  
RUN chown -vfR rundeck:rundeck /opt  
  
USER rundeck  
  
CMD java -jar /opt/rundeck/rundeck.jar

