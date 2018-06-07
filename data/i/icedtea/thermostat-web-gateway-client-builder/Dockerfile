FROM icedtea/thermostat-web-gateway-builder  
  
# Thermostat Web Gateway + Web Client Builder Image.  
# See README.md for environment variables required at runtime.  
ENV THERMOSTAT_VERSION=HEAD \  
APP_USER="default"  
LABEL io.k8s.description="A monitoring and serviceability tool for OpenJDK." \  
io.k8s.display-name="Thermostat Web Gateway + Web Client"  
  
USER root  
  
# Install required RPMs and ensure that the packages were installed  
RUN INSTALL_PKGS="rh-nodejs6 rh-nodejs6-npm" && \  
yum install -y --setopt=tsflags=nodocs ${INSTALL_PKGS} && \  
rpm -V ${INSTALL_PKGS} && \  
yum clean all -y  
  
# Add MongoDB collection to those enabled by the base image  
ENV ENABLED_COLLECTIONS="${ENABLED_COLLECTIONS} rh-nodejs6"  
# Package to install npm packages one at a time, for low memory containers  
RUN scl enable rh-nodejs6 "npm install -g npm-install-que"  
  
WORKDIR ${HOME}  
  
# Install s2i build scripts  
COPY ./s2i/bin/ ${STI_SCRIPTS_PATH}/webclient  
  
# Ensure any UID can read/write to files in /opt/app-root  
RUN chown -R ${APP_USER}:0 /opt/app-root && \  
find /opt/app-root -type d -exec chmod g+rwx '{}' \; && \  
find /opt/app-root -type f -exec chmod g+rw '{}' \;  
  
# User ID of user in base image  
USER 1001  
# Set the default CMD to print the usage of the image, if somebody does docker
run  
CMD "${STI_SCRIPTS_PATH}/webclient/usage"  

