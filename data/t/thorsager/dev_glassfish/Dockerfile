# Note: The build of this image requires a base image containig  
# - bash  
# - curl  
# - unzip  
# - xmlstartlet  
# - java8 (of some sort)  
FROM openjdk:8-jre-alpine3.7  
MAINTAINER Michael Thorsager, github.com/thorsager  
  
RUN apk --no-cache add xmlstarlet bash openssl ca-certificates wget  
  
ARG
gf_arch_url=http://download.oracle.com/glassfish/4.1.1/release/glassfish-4.1.1.zip  
ARG as_admin_password=glassfish  
  
ENV GLASSFISH_ARCHIVE=glassfish \  
GLASSFISH_URL=${gf_arch_url} \  
DOMAIN_NAME=domain1 \  
INSTALL_DIR=/opt \  
PASSWORD=${as_admin_password}  
ENV GLASSFISH_HOME=${INSTALL_DIR}/${GLASSFISH_ARCHIVE}/glassfish\  
PATH=$PATH:${INSTALL_DIR}/${GLASSFISH_ARCHIVE}/bin  
ENV DEPLOYMENT_DIR=${GLASSFISH_HOME}/domains/${DOMAIN_NAME}/autodeploy  
ENV LOG_DIR=${GLASSFISH_HOME}/domains/${DOMAIN_NAME}/logs  
  
RUN mkdir -p /tmp/__gf && \  
wget -O /tmp/__gf/${GLASSFISH_ARCHIVE}.zip ${GLASSFISH_URL} && \  
cd /tmp/__gf && \  
unzip ${GLASSFISH_ARCHIVE}.zip && \  
rm /tmp/__gf/${GLASSFISH_ARCHIVE}.zip && \  
mkdir -p ${INSTALL_DIR}/${GLASSFISH_ARCHIVE} && \  
cd glassfish* && \  
mv * ${INSTALL_DIR}/${GLASSFISH_ARCHIVE} && \  
rm -rf /tmp/__gf  
  
RUN rm -rf ${LOG_DIR} && ln -s ${LOG_DIR} /log  
RUN echo "--- Setup the password file ---" && \  
echo "AS_ADMIN_PASSWORD=" > /tmp/glassfishpwd && \  
echo "AS_ADMIN_NEWPASSWORD=${PASSWORD}" >> /tmp/glassfishpwd && \  
echo "--- Enable DAS, change admin password, and secure admin access ---" && \  
asadmin \--user=admin \--passwordfile=/tmp/glassfishpwd change-admin-password
--domain_name ${DOMAIN_NAME} && \  
asadmin start-domain ${DOMAIN_NAME} && \  
echo "AS_ADMIN_PASSWORD=${PASSWORD}" > /tmp/glassfishpwd && \  
asadmin \--user=admin \--passwordfile=/tmp/glassfishpwd enable-secure-admin &&
\  
asadmin \--user=admin stop-domain ${DOMAIN_NAME} && \  
rm /tmp/glassfishpwd  
  
  
COPY gf_env.sh gf_init.sh ${GLASSFISH_HOME}/bin/  
EXPOSE 4848 9009 8080 8181 8686  
VOLUME [ "/log" ]  
  
WORKDIR ${GLASSFISH_HOME}/bin  
ENTRYPOINT ["/bin/bash", "./gf_init.sh"]  

