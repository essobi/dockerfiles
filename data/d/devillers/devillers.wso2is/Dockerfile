FROM dockerfile/java:openjdk-7-jdk  
MAINTAINER Martin Devillers  
  
# Download and unzip WSO2 Identity Server  
RUN curl https://dl.dropboxusercontent.com/u/1899283/wso2is/wso2is-5.0.0.zip >
/opt/wso2is.zip && \  
unzip /opt/wso2is.zip -d /opt && \  
rm -f /opt/wso2is.zip  
  
# Setup environment  
ENV CARBON_HOME /opt/wso2is-5.0.0  
ENV PATH $CARBON_HOME/bin:$PATH  
  
# Add MSSQL JDBC driver  
RUN curl https://dl.dropboxusercontent.com/u/1899283/wso2is/jtds-1.3.1.jar >
$CARBON_HOME/repository/components/lib.  
  
EXPOSE 9443  
CMD ["/opt/wso2is-5.0.0/bin/wso2server.sh"]

