FROM java:7  
MAINTAINER Manuel Lara Caro <manuel.lara@gmail.com>  
  
ENV WSO2_GREG_VERSION 5.2.0  
ENV CARBON_HOME /opt/wso2greg-$WSO2_GREG_VERSION  
ENV CARBON_HOST localhost  
ENV CARBON_MGT_HOST localhost  
ENV CARBON_OFFSET 0  
# Clustering configuration  
#ENV CLUSTER_DEPLOYMENT false  
#ENV CLUSTER_DOMAIN wso2.carbon.domain  
#ENV CLUSTER_MEMBER_ROLE standalone  
#ENV CLUSTER_SVN_URL svn://$CARBON_HOST:3690/svn/depsyncrepo  
#ENV CLUSTER_SVN_USER wso2svnuser  
#ENV CLUSTER_SVN_PASS passwd  
# Database configuration  
#ENV SHARED_DATABASE_REGISTRY false  
#ENV SHARED_DATABASE_URL
jdbc:mysql://$CARBON_HOST:3306/regdb?autoReconnect=true&amp;useSSL=false  
#ENV SHARED_DATABASE_USER wso2dcarbon  
#ENV SHARED_DATABASE_PASSWD wso2dcarbon  
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
# WSO2 GReg Installation  
# ---------------------------------------------------  
RUN wget --user-agent="testuser"
\--referer="http://connect.wso2.com/wso2/getform/reg/new_product_download"
http://product-dist.wso2.com/products/governance-
registry/$WSO2_GREG_VERSION/wso2greg-$WSO2_GREG_VERSION.zip -P /opt \  
&& unzip -qq /opt/wso2greg-$WSO2_GREG_VERSION.zip -d /opt/ \  
&& rm -rf /opt/wso2greg-$WSO2_GREG_VERSION.zip  
  
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
  
EXPOSE 9443 9763 8243 8280  
CMD /root/entrypoint.sh

