FROM maven:3.2-jdk-8-onbuild  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
ONBUILD ADD . /usr/src/app  
ONBUILD RUN mvn install  
EXPOSE 8080  
ENTRYPOINT ["java"]  
CMD ["-jar", "-Dspring.profiles.active=test", "target/stowaway-investments-
service.jar"]

