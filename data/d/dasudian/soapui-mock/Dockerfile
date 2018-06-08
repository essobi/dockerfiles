# Dockerfile for building a soapui-runner  
FROM anapsix/alpine-java:jre8  
MAINTAINER Mengz <mz@dasudian.com>  
  
ENV SOAPUI_VERSION="5.2.1" \  
SOAPUI="/opt/soapui" \  
PROJECT_FILE="/root/default-project.xml" \  
MOCKSERVICE_NAME="Default REST MockService" \  
MOCKSERVICE_PORT="8080" \  
MOCK_BIN="mockservicerunner.sh"  
RUN wget
http://cdn01.downloads.smartbear.com/soapui/$SOAPUI_VERSION/SoapUI-$SOAPUI_VERSION-
linux-bin.tar.gz && \  
tar -xzf SoapUI-5.2.1-linux-bin.tar.gz -C /opt/ && \  
mv /opt/SoapUI-5.2.1 /opt/soapui && \  
echo "0 1 * * * rm -f /root/*.log" >> /etc/crontabs/root && \  
rm -f SoapUI-5.2.1-linux-bin.tar.gz  
  
ENV PATH="$PATH:$SOAPUI/bin"  
COPY default-project.xml /root/  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["start"]  

