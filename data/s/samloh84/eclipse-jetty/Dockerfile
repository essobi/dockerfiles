FROM samloh84/oracle-jre:8u131-centos7  
  
ARG VENDOR=eclipse  
ARG PRODUCT=jetty  
ARG PRODUCT_VERSION=9.4.6.v20170531  
ARG TEMP_DIR_ROOT=/tmp/${VENDOR}-${PRODUCT}  
ARG TEMP_DIR=${TEMP_DIR_ROOT}/${PRODUCT_VERSION}  
ARG INSTALL_DIR_ROOT=/opt/${VENDOR}-${PRODUCT}  
ARG INSTALL_DIR=${INSTALL_DIR_ROOT}/${PRODUCT_VERSION}  
  
ARG
JETTY_INSTALL_TAR_GZ_URL="http://central.maven.org/maven2/org/eclipse/jetty/jetty-
distribution/9.4.6.v20170531/jetty-distribution-9.4.6.v20170531.tar.gz"  
ARG JETTY_INSTALL_TAR_GZ=jetty-distribution-9.4.6.v20170531.tar.gz  
ARG JETTY_INSTALL_TAR_GZ_SHA1SUM=3c5baab3f04660e1c2fde5c3ea255ba95f2e28f3  
  
ARG JETTY_GPG_KEYS="FE4B68B4"  
ARG
JETTY_INSTALL_TAR_GZ_ASC_URL="http://central.maven.org/maven2/org/eclipse/jetty/jetty-
distribution/9.4.6.v20170531/jetty-distribution-9.4.6.v20170531.tar.gz.asc"  
ARG JETTY_INSTALL_TAR_GZ_ASC=jetty-distribution-9.4.6.v20170531.tar.gz.asc  
  
USER ${ROOT_UID}  
RUN \  
mkdir -p ${TEMP_DIR} && \  
mkdir -p ${INSTALL_DIR} && \  
pushd ${TEMP_DIR} && \  
curl -LjSs ${JETTY_INSTALL_TAR_GZ_ASC_URL} -o ${JETTY_INSTALL_TAR_GZ_ASC} && \  
curl -LjSs ${JETTY_INSTALL_TAR_GZ_URL} -o ${JETTY_INSTALL_TAR_GZ} && \  
for JETTY_GPG_KEY in ${JETTY_GPG_KEYS}; do gpg --keyserver pool.sks-
keyservers.net --recv-keys ${JETTY_GPG_KEY}; done && \  
gpg --verify ${JETTY_INSTALL_TAR_GZ_ASC} ${JETTY_INSTALL_TAR_GZ} && \  
echo "${JETTY_INSTALL_TAR_GZ_SHA1SUM} ${JETTY_INSTALL_TAR_GZ}" | sha1sum -c -
&& \  
tar -xzf ${TEMP_DIR}/${JETTY_INSTALL_TAR_GZ} \--strip-components=1 -C
${INSTALL_DIR} && \  
fix-ownership ${INSTALL_DIR} && \  
fix-permissions ${INSTALL_DIR} && \  
popd && \  
rm -rf ${TEMP_DIR_ROOT}  
  
  
ENV JAVA ${JAVA_HOME}/bin/java  
ENV JETTY_HOME ${INSTALL_DIR}  
ENV PATH ${JETTY_HOME}/bin:${PATH}  
  
USER ${APP_UID}  
  
EXPOSE 8080  
EXPOSE 8443  
  
WORKDIR ${JETTY_HOME}  
  
CMD ${JETTY_HOME}/bin/jetty.sh run  

