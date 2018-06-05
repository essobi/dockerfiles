FROM maven  
WORKDIR /  
# Config and data  
COPY . .  
#RUN mvn clean install -DskipTests -Dmaven.javadoc.skip=true  
# Execute main UI  
EXPOSE 8080  
#ADD /target/autoindex-0.0.1-SNAPSHOT.jar autoindex-0.0.1-SNAPSHOT.jar  
#ENTRYPOINT ["java","-jar","autoindex-0.0.1-SNAPSHOT.jar"]  
#CMD ["mvn", "clean", "install", "spring-boot:run", "-DskipTests",
"-Dmaven.javadoc.skip=true"]  
CMD ["mvn", "clean", "spring-boot:run"]  

