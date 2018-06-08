FROM centos:7  
FROM python:2.7  
FROM java:openjdk-7-jdk  
  
# Version  
ENV SOAPUI_VERSION 5.3.0  
# Download and unarchive SoapUI  
RUN mkdir -p /opt &&\  
curl
http://cdn01.downloads.smartbear.com/soapui/${SOAPUI_VERSION}/SoapUI-${SOAPUI_VERSION}-linux-
bin.tar.gz \  
| gunzip -c - | tar -xf - -C /opt && \  
ln -s /opt/SoapUI-${SOAPUI_VERSION} /opt/SoapUI  
  
# Set working directory  
WORKDIR /opt/bin  
  
# Set environment  
ENV PATH ${PATH}:/opt/SoapUI/bin  
  
ENTRYPOINT ["/opt/SoapUI/bin/testrunner.sh"]  

