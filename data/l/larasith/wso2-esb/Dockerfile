FROM java:7  
MAINTAINER Manuel Lara Caro <manuel.lara@gmail.com>  
  
ENV WSO2_ESB_VERSION 4.9.0  
ENV CARBON_HOME /opt/wso2esb-$WSO2_ESB_VERSION  
ENV CARBON_HOST localhost  
ENV CARBON_MGT_HOST $CARBON_HOST  
ENV CARBON_OFFSET 0  
# Clustering configuration  
ENV CLUSTER_DEPLOYMENT false  
ENV CLUSTER_DOMAIN wso2.carbon.domain  
ENV CLUSTER_MEMBER_ROLE standalone  
ENV CLUSTER_SVN_URL svn://$CARBON_HOST:3690/svn/depsyncrepo  
ENV CLUSTER_SVN_USER wso2svnuser  
ENV CLUSTER_SVN_PASS passwd  
  
# Database configuration  
ENV DATABASE_SHARED_REGISTRY false  
ENV DATABASE_URL
jdbc:mysql://$CARBON_HOST:3306/regdb?autoReconnect=true&amp;useSSL=false  
ENV DATABASE_USER wso2dbuser  
ENV DATABASE_PASSWD passwd  
  
RUN wget --user-agent="testuser"
\--referer="http://connect.wso2.com/wso2/getform/reg/new_product_download"
http://product-dist.wso2.com/products/enterprise-service-
bus/$WSO2_ESB_VERSION/wso2esb-$WSO2_ESB_VERSION.zip -P /root  
RUN unzip -qq /root/wso2esb-$WSO2_ESB_VERSION.zip -d /opt/  
  
COPY assets/* /root/  
  
EXPOSE 9443 9763 8243 8280  
VOLUME ["${CARBON_HOME}/repository"]  
  
WORKDIR ${CARBON_HOME}  
  
CMD /root/entrypoint.sh

