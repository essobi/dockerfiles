FROM centos/httpd-24-centos7  
  
ENV SUMMARY="Barman Documentation" \  
DESCRIPTION="Barman Documentation as it seen in
http://docs.pgbarman.org/release/2.3/ \  
The image is based on centos/httpd-24-centos7 to run unprivileged httpd
container."  
LABEL summary="$SUMMARY" \  
description="$DESCRIPTION" \  
io.k8s.description="$DESCRIPTION" \  
io.k8s.display-name="Barman Documentation" \  
io.openshift.expose-services="8080:http,8443:https" \  
io.openshift.tags="documentation,docs,barman" \  
name="dockerized-docs/barman" \  
maintainer="Genadi Postrilko <genadipost@gmail.com>"  
  
ENV BARMAN_VERSION 2.3  
user root  
  
# Install httrack to download docs  
RUN yum -y install httrack  
  
USER default  
  
# Download barman docs site  
RUN mkdir -p /opt/app-root/src/barman-docs \  
&& cd /opt/app-root/src/barman-docs && httrack
http://docs.pgbarman.org/release/$BARMAN_VERSION \  
&& mv docs.pgbarman.org/release/$BARMAN_VERSION/* /var/www/html/  
  
CMD ["/usr/bin/run-httpd"]  

