FROM alpine:3.7  
  
ARG user_uid=1000  
ARG user_gid=1000  
ARG a4c_ver=2.0.0  
ENV A4C_PORT 8088  
ENV A4C_INSTALL_PATH /opt  
ENV A4C_INSTALL_DIR a4c  
ENV USER a4c  
  
ADD indigodc-orchestrator-plugin "${A4C_INSTALL_PATH}/indigodc-orchestrator-
plugin"  
ADD indigodc-2-a4c.py "${A4C_INSTALL_PATH}"  
  
RUN apk add --no-cache openjdk8-jre-base bash \  
# Install those dependencies that will be removed afterwards  
&& apk --no-cache add --virtual build-dependencies \  
libcurl libssh2 curl expat pcre2 git zip libxau libbsd libxdmcp libxcb libx11
libxcomposite libxext libxi libxrender libxtst alsa-lib libbz2 libpng freetype
giflib openjdk8-jre openjdk8 maven gdbm xz-libs python3 yaml py3-yaml \  
# Get Alien 4 Cloud  
&& cd ${A4C_INSTALL_PATH} \  
&& curl -k -O
https://fastconnect.org/maven/service/local/repositories/opensource/content/alien4cloud/alien4cloud-
dist/${a4c_ver}/alien4cloud-dist-${a4c_ver}-dist.tar.gz \  
&& tar xvf alien4cloud-dist-${a4c_ver}-dist.tar.gz \  
&& mv alien4cloud "${A4C_INSTALL_PATH}/${A4C_INSTALL_DIR}" \  
&& rm alien4cloud-dist-${a4c_ver}-dist.tar.gz \  
# Get and add the IndigoDC Tosca types  
&& git clone -b devel_deep https://github.com/indigo-dc/tosca-types indigo-dc-
tosca-types \  
&& python3 indigodc-2-a4c.py ${A4C_INSTALL_PATH}/indigo-dc-tosca-types/ <
${A4C_INSTALL_PATH}/indigo-dc-tosca-types/custom_types.yaml >
${A4C_INSTALL_PATH}/indigo-dc-tosca-types/tosca_types_alien.yaml \  
&& cd "${A4C_INSTALL_PATH}/indigo-dc-tosca-types" \  
&& zip -9 -r --exclude=custom*
"${A4C_INSTALL_PATH}/${A4C_INSTALL_DIR}/init/archives/indigo-dc-tosca-
types.zip" *.* artifacts/ images/ \  
&& rm -R "${A4C_INSTALL_PATH}/indigo-dc-tosca-types" \  
# Compile and install the plugin  
&& cd "${A4C_INSTALL_PATH}/indigodc-orchestrator-plugin" \  
&& mvn -e clean package \  
&& cp ${A4C_INSTALL_PATH}/indigodc-orchestrator-plugin/target/alien4cloud-
indigodc-provider-*.zip "${A4C_INSTALL_PATH}/${A4C_INSTALL_DIR}/init/plugins/"
\  
&& mvn dependency:purge-local-repository -DactTransitively=false
-DreResolve=false \  
&& rm -R $HOME/.m2 \  
&& rm -R ${A4C_INSTALL_PATH}/indigodc-orchestrator-plugin \  
# Create a special user with limited access  
&& addgroup -g ${user_gid} -S ${USER} \  
&& adduser -D -g "" -u ${user_uid} -G ${USER} ${USER} \  
&& chown -R ${USER}:${USER} "${A4C_INSTALL_PATH}" \  
&& chown -R ${USER}:${USER} "/home/${USER}" \  
# Clean up the installed packages  
&& apk del build-dependencies  
  
EXPOSE ${A4C_PORT}  
  
USER ${USER}  
  
ENTRYPOINT cd ${A4C_INSTALL_PATH}/${A4C_INSTALL_DIR} && ./alien4cloud.sh  

