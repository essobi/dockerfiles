# jekyll-nginx-18-centos7  
FROM centos/nginx-18-centos7  
  
MAINTAINER Josh Preston <the@mrjoshuap.com>  
  
ENV BUILDER_VERSION 1.0  
  
# Set labels used in OpenShift to describe the builder image  
LABEL io.k8s.description="Builder for Jekyll based static sites" \  
io.k8s.display-name="jekyll" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="jekyll,ruby-22,nginx-18,centos"  
# Become the root user  
USER 0  
  
# Copy the S2I scripts from .s2i/bin/ to /usr/libexec/s2i  
COPY ./.s2i/bin/. /usr/libexec/s2i  
  
# Copy the update config file (specifically for software collections)  
COPY ./.s2i/etc/. /opt/app-root/etc  
  
# Install required packages here:  
RUN yum install -y \  
rh-ruby22 \  
rh-ruby22-ruby-devel \  
rh-ruby22-rubygem-bundler \  
&& yum clean all -y  
  
# Drop the root user and make the content of /opt/app-root owned by user 1001  
RUN chown -R 1001:1001 /opt/app-root  
  
# This default user is created in the openshift/base-centos7 image  
USER 1001  
  
# Set the default port for applications built using this image  
EXPOSE 8080  
  
# Set the default CMD for the image  
CMD ["usage"]  

