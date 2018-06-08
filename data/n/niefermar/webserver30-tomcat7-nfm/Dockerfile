# Copyright 2016 Red Hat  
#  
# Licensed under the Apache License, Version 2.0 (the "License");  
# you may not use this file except in compliance with the License.  
# You may obtain a copy of the License at  
#  
# http://www.apache.org/licenses/LICENSE-2.0  
#  
# Unless required by applicable law or agreed to in writing, software  
# distributed under the License is distributed on an "AS IS" BASIS,  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  
# See the License for the specific language governing permissions and  
# limitations under the License.  
#  
# ------------------------------------------------------------------------  
#  
# Rutas lib de sql y kerberos Dockerfile-rhel7-7.3-82 /opt/webserver/lib  
# Rutas config tomcat /opt/webserver/conf  
# opt/webserver/webappsRutas desplieges /opt/webserver/webapps  
# opt/webserver/webappsRutas desplieges /opt/webserver/webapps  
# This is a Dockerfile SE BASA EN the jboss-
webserver-3/webserver30-tomcat7-openshift  
# Dockerfile-jboss-webserver-3-webserver30-tomcat7-openshift-1  
FROM registry.access.redhat.com/jboss-
webserver-3/webserver30-tomcat7-openshift  
MAINTAINER nfernandez@dacartec.com  
EXPOSE 8080  
# Environment variables  
ENV DEPLOY_DIR /deployments  
ENV JBOSS_IMAGE_NAME="niefermar/webserver30-tomcat7-nfm" \  
JBOSS_IMAGE_VERSION="1.0" \  
JBOSS_IMAGE_RELEASE="3" \  
STI_BUILDER="jee"  
# Add lib  
ADD spnego.jar /opt/webserver/lib/  
# Add lib  
ADD sqljdbc4.jar /opt/webserver/lib/  
# Add roles  
ADD tomcat-users.xml /opt/webserver/conf/  
# Add spnego  
ADD login.conf /opt/webserver/conf/  
ADD krb5.conf /opt/webserver/conf/  
  
# Add war  
ADD ROOT.war /opt/webserver/webapps/  
ADD spnego.war /opt/webserver/webapps/  
ADD DPIDemoWebService.war /opt/webserver/webapps/  
ADD deploy-and-run.sh /opt/webserver/bin/  
  
# Labels  
LABEL name="$JBOSS_IMAGE_NAME" \  
version="$JBOSS_IMAGE_VERSION" \  
release="$JBOSS_IMAGE_RELEASE" \  
architecture="x86_64" \  
com.redhat.component="jboss-webserver-3-webserver30-tomcat7-openshift-docker"
\  
io.k8s.description="Platform for building and running web applications on
JBoss Web Server 3.0 - Tomcat v7 spnego" \  
io.k8s.display-name="JBoss Web Server 3.0 spnego" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,java,tomcat7,spnego" \  
io.openshift.s2i.scripts-url="image:///usr/local/s2i"  
  
# Exposed ports  
EXPOSE 8443 8778  
CMD ["/opt/webserver/bin/catalina.sh", "stop"]  
CMD ["/opt/webserver/bin/launch.sh"]  
  
USER root  
  
  
  

