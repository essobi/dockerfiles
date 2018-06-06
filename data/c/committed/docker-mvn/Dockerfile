FROM maven:3-jdk-8  
COPY pom.xml /var/cache/m2/pom.xml  
RUN mvn -Dmaven.repo.local=/var/cache/m2 dependency:go-offline -f
/var/cache/m2/pom.xml  
  
CMD ["mvn", "-Dmaven.repo.local=/var/cache/m2"]  

