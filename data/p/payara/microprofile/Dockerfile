FROM openjdk:8-jdk-alpine  
  
ENV PAYARA_PATH /opt/payara  
  
RUN apk update \  
&& apk add ca-certificates wget \  
&& update-ca-certificates && \  
mkdir -p $PAYARA_PATH/deployments && \  
adduser -D -h $PAYARA_PATH payara && echo payara:payara | chpasswd && \  
chown -R payara:payara /opt  
  
ENV PAYARA_PKG http://repo1.maven.org/maven2/fish/payara/extras/payara-
microprofile/1.0-4.1.2.172/payara-microprofile-1.0-4.1.2.172.jar  
ENV PKG_FILE_NAME payara-microprofile.jar  
ENV PAYARA_VERSION 172  
RUN wget --quiet -O $PAYARA_PATH/$PKG_FILE_NAME $PAYARA_PKG  
  
ENV DEPLOY_DIR $PAYARA_PATH/deployments  
ENV AUTODEPLOY_DIR $PAYARA_PATH/deployments  
ENV PAYARA_MICROPROFILE_JAR=$PAYARA_PATH/$PKG_FILE_NAME  
  
# Default payara ports to expose  
EXPOSE 4848 8009 8080 8181  
USER payara  
WORKDIR $PAYARA_PATH  
  
ENTRYPOINT ["java", "-jar", "/opt/payara/payara-microprofile.jar"]  
CMD ["--deploymentDir", "/opt/payara/deployments"]

