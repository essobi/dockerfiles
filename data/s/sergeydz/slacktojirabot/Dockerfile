FROM maven:3.3.9-jdk-8-onbuild  
COPY . /usr/src/bot  
WORKDIR /usr/src/bot  
RUN mvn package  
ENV slackkey=0  
ENV jirauser=sd  
ENV jirapassword=12345  
ENV slackchannels=artifactory  
CMD ["java", "-jar", "target/SlackToJiraBot-1.0-jar-with-dependencies.jar"]  

