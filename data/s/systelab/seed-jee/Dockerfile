### STAGE 1: Build ###  
# We label our stage as 'builder'  
FROM maven:alpine as builder  
  
## Storing node modules on a separate layer will prevent unnecessary npm
installs at each build  
RUN mkdir /seed-jee  
  
WORKDIR /seed-jee  
  
COPY . .  
  
## Build the angular app in production mode and store the artifacts in dist
folder  
RUN mvn package  
  
### STAGE 2: Setup ###  
FROM jboss/wildfly:12.0.0.Final  
  
COPY docker/customization /opt/jboss/wildfly/customization/  
  
COPY \--from=builder /seed-jee/target/seed.war
/opt/jboss/wildfly/customization/  
  
USER root  
  
RUN chmod +x /opt/jboss/wildfly/customization/wait-for-it.sh  
  
USER jboss  
  
CMD ["/opt/jboss/wildfly/customization/execute.sh"]  

