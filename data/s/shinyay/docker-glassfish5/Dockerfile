FROM store/oracle/serverjre:8  
  
# Maintainer  
MAINTAINER shinyay <shinya.com@gmail.com>  
  
# Set environment variables and default password for user 'admin'  
ENV GLASSFISH_PKG=latest-glassfish.zip \  
GLASSFISH_URL=http://download.oracle.com/glassfish/5.0/nightly \  
GLASSFISH_HOME=/glassfish5 \  
PATH=$PATH:/glassfish5/bin \  
PASSWORD=glassfish  
  
# Install packages, download and extract GlassFish  
# Setup password file  
# Enable DAS  
RUN yum install -y wget unzip && \  
wget --no-check-certificate ${GLASSFISH_URL}/${GLASSFISH_PKG} && \  
unzip -o ${GLASSFISH_PKG} && \  
rm -f ${GLASSFISH_PKG} && \  
yum remove -y wget unzip && \  
echo "----- CREATE PASSWORD FILE --------------------" && \  
echo "AS_ADMIN_PASSWORD=" > /tmp/gfpassword && \  
echo "AS_ADMIN_NEWPASSWORD=${PASSWORD}" >> /tmp/gfpassword && \  
echo "----- CHANGE ADMIN PASSWORD AND SECURE ADMIN ACCESS
--------------------" && \  
asadmin \--user=admin \--passwordfile=/tmp/gfpassword change-admin-password
--domain_name domain1 && \  
echo "----- ENABLE DOMAIN ADMINISTRATION SERVER --------------------" && \  
asadmin start-domain && \  
echo "AS_ADMIN_PASSWORD=${PASSWORD}" > /tmp/gfpassword && \  
asadmin \--user=admin \--passwordfile=/tmp/gfpassword enable-secure-admin && \  
asadmin \--user=admin stop-domain  
  
# Ports being exposed  
EXPOSE 4848 8080 8181  
  
# Start asadmin console and the domain  
CMD ["asadmin", "start-domain", "-v"]  

