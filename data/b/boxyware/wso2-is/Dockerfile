FROM java:7  
MAINTAINER Manuel Lara Caro <manuel.lara@gmail.com>  
  
ENV WSO2_IS_VERSION 5.1.0  
ENV WSO2_AM_VERSION 1.10.0  
ENV CARBON_HOME /opt/wso2is-$WSO2_IS_VERSION  
ENV CARBON_HOST localhost  
ENV CARBON_MGT_HOST localhost  
ENV CARBON_OFFSET 0  
# ---------------------------------------------------  
# WSO2 Databases configuration  
# ---------------------------------------------------  
# Registry  
ENV REG_DATABASE_URL
jdbc:mysql://$CARBON_HOST:3306/regdb?autoReconnect=true&amp;useSSL=false  
ENV REG_DATABASE_USER wso2dcarbon  
ENV REG_DATABASE_PASSWD wso2dcarbon  
# User Management  
ENV UM_DATABASE_URL null  
ENV UM_DATABASE_USER null  
ENV UM_DATABASE_PASSWD null  
# API Management and Identities  
ENV AM_DATABASE_URL null  
ENV AM_DATABASE_USER null  
ENV AM_DATABASE_PASSWD null  
  
# ---------------------------------------------------  
# Integrations  
# ---------------------------------------------------  
ENV API_GATEWAY_HOST null  
  
# ---------------------------------------------------  
# WSO2 Identity Server Installation  
# ---------------------------------------------------  
#RUN wget --user-agent="testuser"
--referer="http://connect.wso2.com/wso2/getform/reg/new_product_download"
http://product-dist.wso2.com/products/identity-
server/$WSO2_IS_VERSION/wso2is-$WSO2_IS_VERSION.zip -P /opt \  
RUN wget --user-agent="testuser"
\--referer="http://connect.wso2.com/wso2/getform/reg/new_product_download"
http://product-dist.wso2.com/downloads/api-manager/$WSO2_AM_VERSION/identity-
server/wso2is-$WSO2_IS_VERSION.zip -P /opt \  
&& unzip -qq /opt/wso2is-$WSO2_IS_VERSION.zip -d /opt/ \  
&& rm -rf /opt/wso2is-$WSO2_IS_VERSION.zip  
  
# ---------------------------------------------------  
# MySQL Driver installation  
# ---------------------------------------------------  
RUN wget http://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-
java-5.1.38.zip -P /root \  
&& unzip /root/mysql-connector-java-5.1.38.zip mysql-connector-
java-5.1.38/mysql-connector-java-5.1.38-bin.jar -d /root/ \  
&& mv /root/mysql-connector-java-5.1.38/mysql-connector-java-5.1.38-bin.jar
$CARBON_HOME/repository/components/lib \  
&& rm -rf /root/mysql-connector-java-5.1.38*  
  
COPY assets/* /root/  
  
EXPOSE 9443 9763  
CMD /root/entrypoint.sh

