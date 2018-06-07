# WSO2 Enterprise Integrator Docker Image  
#  
# License: GNU Lesser General Public License (LGPL), version 3 or later  
# See the LICENSE file in the root directory or
<http://www.gnu.org/licenses/lgpl-3.0.html>.  
FROM openjdk:alpine  
MAINTAINER Bruno Cesar <bruno@modoagil.com.br>  
  
WORKDIR /opt  
  
ARG EI_VERSION=6.1.1  
ARG PRODUCT_NAME=wso2ei  
ARG ZIP_URL=https://product-dist.wso2.com/products/enterprise-
integrator/$EI_VERSION/$PRODUCT_NAME-$EI_VERSION.zip  
  
RUN apk add --update curl unzip; \  
curl -LOk -A "testuser" -e
"http://connect.wso2.com/wso2/getform/reg/new_product_download" $ZIP_URL; \  
unzip -qq $PRODUCT_NAME-$EI_VERSION.zip; \  
mv $PRODUCT_NAME-$EI_VERSION $PRODUCT_NAME; \  
rm -f $PRODUCT_NAME/bin/*.bat; \  
rm -f wso2*.zip  
  
ENV CARBON_HOME /opt/$PRODUCT_NAME  
ENV PATH $PATH:$CARBON_HOME/bin:$JAVA_HOME/bin  
  
WORKDIR /  
  
EXPOSE 8280 8243 9443  
ENTRYPOINT ["integrator.sh"]  

