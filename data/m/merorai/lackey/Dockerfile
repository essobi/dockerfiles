FROM openjdk:8-jdk-alpine  
  
ENV PAYARA_PATH /opt/payara  
  
RUN apk update\  
&& apk add ca-certificates wget \  
&& update-ca-certificates && \  
mkdir -p $PAYARA_PATH/deployments && \  
adduser -D -h $PAYARA_PATH payara && echo payara:payara | chpasswd && \  
chown -R payara:payara /opt  
  
ENV PAYARA_PKG https://github.com/MeroRai/demo/blob/master/payara-
micro.jar?raw=true  
ENV PKG_FILE_NAME payara-micro.jar  
  
RUN wget --quiet -O $PAYARA_PATH/$PKG_FILE_NAME $PAYARA_PKG  
  
RUN wget --quiet -O ${PAYARA_PATH}/LackeyModule.war
https://github.com/MeroRai/demo/blob/master/LackeyModule.war?raw=true  
RUN wget --quiet -O ${PAYARA_PATH}/healthcheck.txt
https://raw.githubusercontent.com/MeroRai/demo/master/healthcheck.txt  
RUN wget --quiet -O ${PAYARA_PATH}/hz.xml
https://raw.githubusercontent.com/MeroRai/demo/master/hz.xml  
  
# Default payara ports to expose  
EXPOSE 4848 8009 8080 8181  
USER payara  
WORKDIR $PAYARA_PATH  
  
ENTRYPOINT ["java", "-jar", "payara-micro.jar", "--hzconfigfile", "hz.xml", "
--deploy", "LackeyModule.war", "--port", "8083", "--autobindhttp", "--name",
"Lackey"]  
  

