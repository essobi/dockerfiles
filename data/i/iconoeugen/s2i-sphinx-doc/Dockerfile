FROM openshift/base-centos7  
MAINTAINER Horatiu Vlad <horatiu@vlad.eu>  
  
EXPOSE 8080  
  
ENV PATH ${HOME}/.local/bin/:$PATH  
  
LABEL io.k8s.description="Platform for building and running Sphinx
documentation" \  
io.k8s.display-name="Spinx 1.5" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="builder,sphinx,python,python36,rh-python36"  
RUN yum install -y centos-release-scl-rh && \  
yum-config-manager --enable centos-sclo-rh-testing && \  
INSTALL_PKGS="rh-python36 rh-python36-python-devel rh-python36-python-
setuptools rh-python36-python-pip rh-python36-python-sphinx.noarch nss_wrapper
atlas-devel gcc-gfortran" && \  
yum install -y \--setopt=tsflags=nodocs \--enablerepo=centosplus
${INSTALL_PKGS} && \  
rpm -V ${INSTALL_PKGS} && \  
yum clean all -y  
  
# Copy the S2I scripts from the specific language image to
${STI_SCRIPTS_PATH}.  
COPY ./.s2i/bin/ ${STI_SCRIPTS_PATH}  
# Each language image can have 'contrib' a directory with extra files needed
to  
# run and build the applications.  
COPY ./contrib/ /opt/app-root  
  
# In order to drop the root user, we have to make some directories world  
# writable as OpenShift default security model is to run the container under  
# random UID.  
RUN chown -R 1001:0 /opt/app-root && chmod -R og+rwX /opt/app-root  
  
USER 1001  
  
# Set the default CMD to print the usage of the language image.  
CMD ${STI_SCRIPTS_PATH}/usage  

