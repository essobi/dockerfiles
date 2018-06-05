FROM java:8  
# Install Gradle  
RUN wget https://services.gradle.org/distributions/gradle-2.0-bin.zip  
RUN unzip gradle-2.0-bin.zip  
RUN mv gradle-2.0 /opt/  
RUN rm gradle-2.0-bin.zip  
  
# Environment variables  
ENV GRADLE_HOME /opt/gradle-2.0  
ENV PATH $PATH:$GRADLE_HOME/bin  
  
COPY spring-boot-hello-world /opt/spring-boot-hello-world  
  
WORKDIR /opt/spring-boot-hello-world  
  
RUN gradle build  
  
EXPOSE 8080  
CMD ["java", "-jar", "build/libs/gs-spring-boot-hello-world-0.1.0.jar"]

