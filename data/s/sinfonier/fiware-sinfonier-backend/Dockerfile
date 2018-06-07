FROM maven:3.3.9-jdk-8-alpine  
  
RUN apk add --no-cache bash git openssh  
  
ENV MVN_TARGET_HOST=artifactory  
ENV MVN_TARGET_PORT=8081  
ENV MVN_TARGET_USER=admin  
ENV MVN_TARGET_PASSWORD=password  
ENV MVN_TARGET_ID=central  
ENV MVN_TARGET_NAME=libs-release  
ENV MVN_TARGET_URL_PATH=artifactory/libs-release  
ENV MVN_TARGET_URL_LOCAL_PATH=artifactory/libs-release-local  
  
RUN git clone https://github.com/telefonicaid/fiware-sinfonier.git && cd
fiware-sinfonier && git checkout $SOURCE_BRANCH  
WORKDIR /fiware-sinfonier/sinfonier-backend  
RUN mvn compile package  
COPY /settings.xml /root/.m2/settings.xml  
COPY /setup.sh /root/setup.sh  
RUN chmod +x /root/setup.sh  
  
ENTRYPOINT ["/root/setup.sh"]  

