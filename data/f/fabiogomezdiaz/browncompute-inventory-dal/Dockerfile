# STAGE: Build  
FROM ibmcase/gradle:latest as builder  
  
# Copy Code Over  
RUN mkdir /dalapp  
WORKDIR /dalapp  
COPY . /dalapp  
  
# Build jar  
RUN gradle build  
  
# STAGE: Deploy  
FROM websphere-liberty:webProfile7  
MAINTAINER https://github.com/ibm-cloud-architecture - IBM - Jerome Boyer -
Fabio Gomez  
RUN installUtility install --acceptLicense jpa-2.0 jaxws-2.2 adminCenter-1.0  
  
# Create Directory  
RUN mkdir /opt/ibm/wlp/usr/shared/config/lib  
  
# Add jar and war files  
COPY \--from=builder /dalapp/src/main/liberty/config/server.xml
/opt/ibm/wlp/usr/servers/defaultServer  
COPY \--from=builder /dalapp/lib/db2jcc4.jar
/opt/ibm/wlp/usr/shared/config/lib  
COPY \--from=builder /dalapp/build/libs/refarch-integration-inventory-dal.war
/opt/ibm/wlp/usr/servers/defaultServer/apps  
  
# Set Port  
EXPOSE 9080 9443  
# Start  
ENTRYPOINT ["/opt/ibm/wlp/bin/server", "run", "defaultServer"]

