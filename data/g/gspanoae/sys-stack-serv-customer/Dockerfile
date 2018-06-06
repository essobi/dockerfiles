FROM maven:3.5.0-jdk-8-alpine  
  
# ###################################  
# Image core configuration  
# ###################################  
# Configure image arguments  
ARG SPRING_APPLICATION_NAME  
ARG SPRING_PROFILES_ACTIVE  
ARG SPRING_CLOUD_CONFIG_URI  
ARG SPRING_CLOUD_CONFIG_USERNAME  
ARG SPRING_CLOUD_CONFIG_PASSWORD  
ARG SPRING_CLOUD_CONFIG_FAILFAST  
ARG SPRING_CLOUD_CONFIG_RETRY_INITIALINTERVAL  
ARG SPRING_CLOUD_CONFIG_RETRY_MULTIPLIER  
ARG SPRING_CLOUD_CONFIG_RETRY_MAXATTEMPTS  
# Assign arguments to environment  
ENV SPRING_APPLICATION_NAME=$SPRING_APPLICATION_NAME
SPRING_PROFILES_ACTIVE=$SPRING_PROFILES_ACTIVE
SPRING_CLOUD_CONFIG_URI=$SPRING_CLOUD_CONFIG_URI
SPRING_CLOUD_CONFIG_USERNAME=$SPRING_CLOUD_CONFIG_USERNAME
SPRING_CLOUD_CONFIG_PASSWORD=$SPRING_CLOUD_CONFIG_PASSWORD
SPRING_CLOUD_CONFIG_FAILFAST=$SPRING_CLOUD_CONFIG_FAILFAST
SPRING_CLOUD_CONFIG_RETRY_INITIALINTERVAL=$SPRING_CLOUD_CONFIG_RETRY_INITIALINTERVAL
SPRING_CLOUD_CONFIG_RETRY_MULTIPLIER=$SPRING_CLOUD_CONFIG_RETRY_MULTIPLIER
SPRING_CLOUD_CONFIG_RETRY_MAXATTEMPTS=$SPRING_CLOUD_CONFIG_RETRY_MAXATTEMPTS  
# Configure service workspace folder  
RUN mkdir -p workspace/sys-stack-serv-customer  
# Add service files  
ADD . /workspace/sys-stack-serv-customer  
  
# ###################################  
# Install 3rd party dependencies  
# ###################################  
# Install JCE  
WORKDIR /workspace/sys-stack-serv-
customer/src/main/resources/vendor/oracle/JCE/  
RUN unzip UnlimitedJCEPolicyJDK7.zip && \  
cp /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/local_policy.jar
/usr/lib/jvm/java-1.8-openjdk/jre/lib/security/local_policy.jar.bak && \  
cp /usr/lib/jvm/java-1.8-openjdk/jre/lib/security/US_export_policy.jar
/usr/lib/jvm/java-1.8-openjdk/jre/lib/security/US_export_policy.jar.bak && \  
cp UnlimitedJCEPolicy/local_policy.jar
/usr/lib/jvm/java-1.8-openjdk/jre/lib/security/local_policy.jar && \  
cp UnlimitedJCEPolicy/US_export_policy.jar
/usr/lib/jvm/java-1.8-openjdk/jre/lib/security/US_export_policy.jar && \  
rm -rf UnlimitedJCEPolicy  
  
# ###################################  
# Package build  
# ###################################  
# Build source code using Maven with dev profile/arguments  
WORKDIR /workspace/sys-stack-serv-customer  
RUN mvn \  
-DSPRING_APPLICATION_NAME=customer \  
-DSPRING_PROFILES_ACTIVE=dev \  
-DSPRING_CLOUD_CONFIG_URI=http://127.0.0.1:9999 \  
-DSPRING_CLOUD_CONFIG_USERNAME=admin \  
-DSPRING_CLOUD_CONFIG_PASSWORD=q1w2e3r4T% \  
-DSPRING_CLOUD_CONFIG_FAILFAST=false \  
-DSPRING_CLOUD_CONFIG_RETRY_INITIALINTERVAL=1000 \  
-DSPRING_CLOUD_CONFIG_RETRY_MULTIPLIER=1.1 \  
-DSPRING_CLOUD_CONFIG_RETRY_MAXATTEMPTS=3 \  
clean package install  
  
# ###################################  
# Declare image ports and entry-points  
# ###################################  
# Expose service ports for each profile (5010 for dev, 7010 for test and 8010
for prod)  
EXPOSE 5010 7010 8010  
# Define image entry-points  
RUN ["chmod", "+x", "./docker-entrypoint.sh"]  
ENTRYPOINT [ "/bin/bash", "-l", "./docker-entrypoint.sh" ]  

