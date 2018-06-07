FROM icedtea/openjdk-8-64bit-maven  
  
# Thermostat Web Gateway Builder Image.  
# See README.md for environment variables required at runtime.  
ENV THERMOSTAT_VERSION=HEAD \  
APP_USER="default"  
LABEL io.k8s.description="A monitoring and serviceability tool for OpenJDK." \  
io.k8s.display-name="Thermostat Web Gateway"  
  
ENV THERMOSTAT_GATEWAY_HOME /opt/app-root/thermostat  
  
USER root  
  
# Ensure THERMOSTAT_GATEWAY_HOME (and parents) exist  
RUN mkdir -p ${THERMOSTAT_GATEWAY_HOME}  
  
# Install required RPMs and ensure that the packages were installed  
RUN INSTALL_PKGS="rh-mongodb32 rh-mongodb32-mongodb" && \  
yum install -y --setopt=tsflags=nodocs ${INSTALL_PKGS} && \  
rpm -V ${INSTALL_PKGS} && \  
yum clean all -y  
  
# Add MongoDB collection to those enabled by the base image  
ENV ENABLED_COLLECTIONS="${ENABLED_COLLECTIONS} rh-mongodb32"  
WORKDIR ${HOME}  
  
# Install s2i build scripts  
COPY ./s2i/bin/ ${STI_SCRIPTS_PATH}  
  
# Use a dedicated subdirectory for builds to avoid conflict with m2 cache  
ENV THERMOSTAT_BUILD_DIR="${HOME}/thermostat-build"  
# Ensure any UID can read/write to files in /opt/app-root  
RUN chown -R ${APP_USER}:0 /opt/app-root && \  
find /opt/app-root -type d -exec chmod g+rwx '{}' \; && \  
find /opt/app-root -type f -exec chmod g+rw '{}' \;  
  
COPY ./bin /usr/bin  
  
# User ID of user in base image  
USER 1001  
# Specify the ports the final image will expose  
EXPOSE 30000  
ENTRYPOINT [ "container-entrypoint" ]  
# Set the default CMD to print the usage of the image, if somebody does docker
run  
CMD "${STI_SCRIPTS_PATH}/usage"  

