FROM icedtea/openjdk-8-64bit-maven  
  
# Thermostat Agent Builder Image.  
# See README.md for environment variables required at runtime.  
ENV THERMOSTAT_VERSION=HEAD \  
APP_USER="default"  
LABEL io.k8s.description="A monitoring and serviceability tool for OpenJDK." \  
io.k8s.display-name="Thermostat Agent"  
  
ENV THERMOSTAT_HOME /opt/app-root/thermostat  
ENV USER_THERMOSTAT_HOME /opt/app-root/.thermostat  
  
USER root  
  
# Ensure THERMOSTAT_HOME (and parents) exist  
RUN mkdir -p ${THERMOSTAT_HOME}  
  
# Install required RPMs and ensure that the packages were installed  
RUN INSTALL_PKGS="autoconf automake make gcc" && \  
yum install -y --setopt=tsflags=nodocs ${INSTALL_PKGS} && \  
rpm -V ${INSTALL_PKGS} && \  
yum clean all -y  
  
WORKDIR ${HOME}  
  
COPY ./thermostat-user-home-config ${USER_THERMOSTAT_HOME}  
  
# Install s2i build scripts without overwriting those from the base image  
COPY ./s2i/bin/ ${STI_SCRIPTS_PATH}/agent  
# Use Thermostat agent S2I scripts by default  
LABEL io.openshift.s2i.scripts-url="image://${STI_SCRIPTS_PATH}/agent"  
# Use an environment variable for S2I destination, which child images should  
# override if they wish to use a different destination  
ENV THERMOSTAT_SOURCE_DIR="/tmp"  
LABEL io.openshift.s2i.destination="${THERMOSTAT_SOURCE_DIR}"  
# Use a build directory specifically for the agent  
ENV THERMOSTAT_BUILD_DIR="${HOME}/thermostat-build"  
# Ensure any UID can read/write to files in /opt/app-root  
RUN chown -R ${APP_USER}:0 /opt/app-root && \  
find /opt/app-root -type d -exec chmod g+rwx '{}' \; && \  
find /opt/app-root -type f -exec chmod g+rw '{}' \;  
  
COPY ./bin /usr/bin  
  
# Remove any potential Hotspot perf data files  
RUN rm -rf /tmp/hsperfdata_*  
  
# User ID of user in base image  
USER 1001  
ENTRYPOINT [ "container-entrypoint" ]  
CMD [ "bash", "-c", "${STI_SCRIPTS_PATH}/agent/usage" ]  

