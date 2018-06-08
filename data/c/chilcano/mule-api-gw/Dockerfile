# Dockerfile to create a MuleSoft Anypoint API Gateway  
FROM java  
  
MAINTAINER Roger CARHUATOCTO <chilcano at intix dot info>  
  
ENV MULE_BUNDLE_NAME=api-gateway-distribution-standalone-2.2.0  
ENV MULE_DIR_NAME=muleapigw  
ENV MULE_HOME /opt/${MULE_DIR_NAME}  
  
WORKDIR /opt  
  
RUN wget -q -P /opt https://s3.amazonaws.com/static-anypoint-mulesoft-
com/${MULE_BUNDLE_NAME}.zip  
RUN unzip /opt/${MULE_BUNDLE_NAME}.zip -d /opt/ >
/opt/${MULE_DIR_NAME}_listfiles  
RUN mv /opt/$(ls -1t|tail -1) /opt/${MULE_DIR_NAME}  
RUN rm /opt/${MULE_BUNDLE_NAME}.zip  
  
# Remote debugger port  
EXPOSE 5000  
# JMX port  
EXPOSE 1098  
# MMC agent port  
EXPOSE 7777  
# API ports  
EXPOSE 8082 8083  
VOLUME ["/opt/${MULE_DIR_NAME}/logs", "/opt/${MULE_DIR_NAME}/conf",
"/opt/${MULE_DIR_NAME}/apps", "/opt/${MULE_DIR_NAME}/domains"]  
  
WORKDIR ${MULE_HOME}  
  
CMD ./bin/gateway  

