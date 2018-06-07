FROM openjdk:8-jre-alpine  
  
ARG WSO2_SERVER_VERSION=${WSO2_SERVER_VERSION:-6.1.1}  
ARG PRODUCT_ID=${PRODUCT_ID:-enterprise-integrator}  
ARG WSO2_SERVER=${WSO2_SERVER:-wso2ei}  
ARG PRODUCT_USER=${PRODUCT_USER:-wso2user}  
ARG PRODUCT_REPOSITORY=${PRODUCT_REPOSITORY:-'https://product-
dist.wso2.com/products'}  
RUN addgroup -S ${PRODUCT_USER} && adduser -S -g ${PRODUCT_USER}
${PRODUCT_USER}  
RUN apk add \--no-cache --update-cache \  
ca-certificates \  
unzip \  
wget \  
&& \  
wget \  
\--progress=dot:giga \  
\--referer="http://connect.wso2.com/wso2/getform/reg/new_product_download" \  
-O "/tmp/${WSO2_SERVER}-${WSO2_SERVER_VERSION}.zip" \   
"${PRODUCT_REPOSITORY}/${PRODUCT_ID}/${WSO2_SERVER_VERSION}/${WSO2_SERVER}-${WSO2_SERVER_VERSION}.zip"
&& \  
unzip /tmp/${WSO2_SERVER}-${WSO2_SERVER_VERSION}.zip -d /opt && \  
chmod o-rwx -R /opt/${WSO2_SERVER}-${WSO2_SERVER_VERSION} && \  
chown ${PRODUCT_USER}:${PRODUCT_USER} -R
/opt/${WSO2_SERVER}-${WSO2_SERVER_VERSION} && \  
rm /tmp/${WSO2_SERVER}-${WSO2_SERVER_VERSION}.zip && \  
apk del \  
ca-certificates \  
unzip \  
wget  
  
USER ${PRODUCT_USER}  
  
EXPOSE 9443 9763 8243 8280  
WORKDIR /opt/${WSO2_SERVER}-${WSO2_SERVER_VERSION}  
ENTRYPOINT ["bin/integrator.sh"]  

