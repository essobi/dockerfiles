FROM centos:centos7  
MAINTAINER Simon Li "spli@dundee.ac.uk"  
ENV RUNDECK_RELEASE 2.6.0-1.11.GA  
# RUN yum -y install http://rundeck.org/latest.rpm && yum -y install rundeck  
RUN yum -y install java-1.8.0-openjdk && \  
yum -y install \  
https://dl.bintray.com/rundeck/rundeck-
rpm/rundeck-${RUNDECK_RELEASE}.noarch.rpm \  
https://dl.bintray.com/rundeck/rundeck-rpm/rundeck-
config-${RUNDECK_RELEASE}.noarch.rpm && \  
yum clean all  
  
RUN yum -y install sudo && \  
yum clean all && \  
echo 'rundeck ALL= (ALL) NOPASSWD: ALL' > /etc/sudoers.d/rundeck && \  
chmod 440 /etc/sudoers.d/rundeck  
  
RUN mkdir -p /rundeck/data /rundeck/projects /rundeck/logs /rundeck/ssh && \  
chown rundeck:rundeck /rundeck/*  
  
USER rundeck  
  
RUN sed -i \  
-e 's|/var/lib/rundeck/data|/rundeck/data|' \  
-e 's|/var/rundeck/projects|/rundeck/projects|' \  
-e 's|/var/lib/rundeck/logs|/rundeck/logs|' \  
-e 's|/var/lib/rundeck/.ssh/id_rsa|/rundeck/ssh/id_rsa|' \  
/etc/rundeck/profile \  
/etc/rundeck/framework.properties \  
/etc/rundeck/rundeck-config.properties && \  
sed -i -re 's|#(.*-Drundeck.ssl.config)|\1|' /etc/rundeck/profile && \  
sed -i -re 's|(grails.serverURL=).*|\1https://localhost:4443|' \  
/etc/rundeck/rundeck-config.properties && \  
sed -i -r -e 's|(framework.server.port\s*=\s*).*|\14443|' \  
-e 's|(framework.server.url\s*=\s*).*|\1https://localhost:4443|' \  
/etc/rundeck/framework.properties  
  
RUN keytool -keystore /etc/rundeck/ssl/keystore -alias rundeck -genkey \  
-keyalg RSA -keypass adminadmin -storepass adminadmin \  
-dname "cn=localhost, o=OME, c=UK" && \  
cp /etc/rundeck/ssl/keystore /etc/rundeck/ssl/truststore && \  
mv /var/lib/rundeck/.ssh/id_rsa* /rundeck/ssh/  
  
ADD run.sh /  
  
VOLUME ["/etc/rundeck", "/rundeck"]  
  
EXPOSE 4440 4443  
CMD /run.sh  

