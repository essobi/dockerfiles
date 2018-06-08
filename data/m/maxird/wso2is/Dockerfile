FROM maxird/java:7-8  
ENV WSO2_VERSION=5.3.0  
ENV WSO2_FOLDER=identity-server  
ENV WSO2_CODE=is  
  
RUN cd /tmp && \  
wget \  
-q \  
\--user-agent=testuser \  
\--referer=https://wso2.com/integration/download-thank-you/ \  
https://product-
dist.wso2.com/products/${WSO2_FOLDER}/${WSO2_VERSION}/wso2${WSO2_CODE}-${WSO2_VERSION}.zip
&& \  
cd /opt && \  
unzip -q /tmp/wso2${WSO2_CODE}-${WSO2_VERSION}.zip && \  
rm -f /tmp/wso2${WSO2_CODE}-${WSO2_VERSION}.zip && \  
echo 'done'  
  
EXPOSE 9443 9763 8000 10500  
WORKDIR /opt/wso2${WSO2_CODE}-${WSO2_VERSION}/bin  
CMD ["./wso2server.sh"]  

