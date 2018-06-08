FROM atlassian/default-image  
  
ENV PAYARA_PKG https://s3-eu-
west-1.amazonaws.com/payara.fish/Payara+Downloads/Payara+4.1.2.174/payara-4.1.2.174.zip  
ENV PAYARA_VERSION 174  
ENV PAYARA_PATH /opt/payara41  
ENV PKG_FILE_NAME payara-full-${PAYARA_VERSION}.zip  
  
# Download Payara Server and install  
RUN \  
wget --quiet -O /opt/${PKG_FILE_NAME} ${PAYARA_PKG} && \  
unzip -qq /opt/${PKG_FILE_NAME} -d /opt  
  
RUN apt-get -y install jq  

