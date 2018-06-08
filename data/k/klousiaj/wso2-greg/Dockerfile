##  
# borrowed liberally from chilcano/wso2am  
##  
FROM klousiaj/oracle-java:7.79  
MAINTAINER J.P. Klousia <klousiaj>  
  
ENV WSO2_BUNDLE_NAME wso2greg-5.3.0  
ENV WSO2_FOLDER_NAME wso2greg  
ENV WSO2_HTTPS_PORT 9444  
ENV WSO2_HTTP_PORT 9764  
ENV WSO2_PORT_OFFSET 1  
# move the file onto the container so it can be unzipped  
RUN wget -q --no-check-certificate -P /opt
https://www.dropbox.com/s/o7pa862pcpt10p6/wso2greg-5.3.0.zip; \  
unzip /opt/$WSO2_BUNDLE_NAME.zip -d /opt/ >
/opt/${WSO2_FOLDER_NAME}.listfiles; \  
mv /opt/${WSO2_BUNDLE_NAME} /opt/${WSO2_FOLDER_NAME}; \  
rm /opt/${WSO2_FOLDER_NAME}.listfiles; \  
rm /opt/${WSO2_BUNDLE_NAME}.zip;  
  
ENV JAVA_HOME /opt/java  
  
# Working Directory in Container  
WORKDIR /opt/${WSO2_FOLDER_NAME}/bin/  
  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
# expose the necessary ports to run the Governance Registry  
EXPOSE ${WSO2_HTTPS_PORT} ${WSO2_HTTP_PORT}  
  
# Start WSO2-GREG  
CMD ["./wso2server.sh"]

