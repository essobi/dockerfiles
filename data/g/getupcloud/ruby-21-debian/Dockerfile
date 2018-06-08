FROM ruby:2.1  
  
# TODO: Put the maintainer name in the image metadata  
MAINTAINER Diego Castro <diego.castro@getupcloud.com>  
  
# TODO: Rename the builder environment variable to inform users about
application you provide them  
  
ENV \  
# DEPRECATED: Use above LABEL instead, because this will be removed in future
versions.  
STI_SCRIPTS_URL=image:///usr/libexec/s2i \  
# Path to be used in other layers to place s2i scripts into  
STI_SCRIPTS_PATH=/usr/libexec/s2i \  
# The $HOME is not set by default, but some applications needs this variable  
HOME=/opt/app-root/src \  
PATH=/opt/app-root/src/bin:/opt/app-root/bin:$PATH \  
RUBY_VERSION=2.1  
  
# TODO: Set labels used in OpenShift to describe the builder image  
LABEL io.k8s.description="Platform for building and running Ruby 2.1
applications" \  
io.k8s.display-name="Ruby 2.1" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,ruby,ruby21" \  
io.openshift.s2i.scripts-url=image:///usr/libexec/s2i  
  
# TODO: Install required packages here:  
RUN apt-get update && apt-get install vim nodejs libv8-dev nginx -y && \  
mkdir -p ${HOME}/.pki/nssdb && \  
chown -R 1001:0 ${HOME}/.pki && \  
useradd -u 1001 -r -g 0 -d ${HOME} -s /sbin/nologin -c "Default Application
User" default  
  
# TODO (optional): Copy the builder files into /opt/app-root  
# COPY ./<builder_folder>/ /opt/app-root/  
# TODO: Copy the S2I scripts to /usr/libexec/s2i, since openshift/base-centos7
image sets io.openshift.s2i.scripts-url label that way, or update that label  
COPY bin/ /usr/bin/  
COPY ./.s2i/bin/ /usr/libexec/s2i  
COPY ./contrib/ /opt/app-root  
  
# TODO: Drop the root user and make the content of /opt/app-root owned by user
1001  
RUN chmod -R a+rwx /opt/app-root/etc && \  
chmod -R a+rwx /var/lib/nginx && \  
chown -R 1001:0 /opt/app-root && \  
chown -R 1001:0 /var/lib/nginx && \  
mkdir -p /var/log/nginx && \  
chown -R 1001:0 /var/log/nginx && \  
chmod -R a+rwx /var/log/nginx  
  
# This default user is created in the openshift/base-centos7 image  
USER 1001  
  
# TODO: Set the default port for applications built using this image  
EXPOSE 8080  
  
# Directory with the sources is set as the working directory so all STI
scripts  
# can execute relative to this path.  
WORKDIR ${HOME}  
  
ENTRYPOINT ["container-entrypoint"]  
CMD ["base-usage"]  

