FROM maxird/java:7-8  
ENV WSO2_VERSION=6.1.1  
ENV WSO2_FOLDER=enterprise-integrator  
ENV WSO2_CODE=ei  
  
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
  
EXPOSE 9443 9763 8243 8280  
WORKDIR /opt/wso2${WSO2_CODE}-${WSO2_VERSION}/bin  
CMD ["./integrator.sh"]  

