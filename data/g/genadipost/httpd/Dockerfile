FROM centos/httpd-24-centos7  
  
ENV SUMMARY="httpd Documentation" \  
DESCRIPTION="httpd Documentation as it seen in
https://httpd.apache.org/docs/2.4/. \  
The image is based on centos/httpd-24-centos7 to run unprivileged httpd
container."  
LABEL summary="$SUMMARY" \  
description="$DESCRIPTION" \  
io.k8s.description="$DESCRIPTION" \  
io.k8s.display-name="httpd Documentation" \  
io.openshift.expose-services="8080:http,8443:https" \  
io.openshift.tags="documentation,docs,httpd" \  
name="genadipost/dockerized-docs-httpd" \  
maintainer="Genadi Postrilko <genadipost@gmail.com>"  
  
ENV HTTPD_VERSION 2.4.33  
USER root  
  
RUN yum -y install wget  
  
USER default  
  
WORKDIR /opt/app-root/src/  
  
RUN wget http://apache.spd.co.il/httpd/docs/httpd-docs-$HTTPD_VERSION.en.zip \  
&& unzip httpd-docs-$HTTPD_VERSION.en.zip \  
&& mv httpd-docs-$HTTPD_VERSION.en/* /var/www/html/ \  
&& rm httpd-docs-$HTTPD_VERSION.en.zip  
  
CMD ["/usr/bin/run-httpd"]  

