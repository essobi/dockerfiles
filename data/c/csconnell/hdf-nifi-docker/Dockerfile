#############################################################  
# A dockerfile for building a NiFi image utilizing a  
# Hortonworks release, specifically 1.5.0.3.1.0.0-564.  
#  
# This dockerfile is based upon the official Apache dockerfile  
# and includes shell scripts from that implementation.  
############################################################  
  
FROM openjdk:8-jre  
LABEL maintainer="CSConnell <csconnell@staq.com>"  
LABEL site="https://www.staq.com"  
  
ARG UID=1000  
ARG GID=1000  
ARG HDF_VERSION=3.1.0.0  
ARG NIFI_VERSION=1.5.0.3.1.0.0-564  
ARG MIRROR=public-repo-1.hortonworks.com  
  
ENV NIFI_BASE_DIR /opt/nifi  
ENV NIFI_HOME=${NIFI_BASE_DIR}/nifi-${NIFI_VERSION} \  
NIFI_BINARY_URL=HDF/${HDF_VERSION}/nifi-${NIFI_VERSION}-bin.tar.gz  
  
  
# Setup NiFi user  
RUN groupadd -g ${GID} nifi || groupmod -n nifi `getent group ${GID} | cut -d:
-f1` \  
&& useradd --shell /bin/bash -u ${UID} -g ${GID} -m nifi \  
&& mkdir -p ${NIFI_HOME}/conf/templates \  
&& chown -R nifi:nifi ${NIFI_BASE_DIR} \  
&& apt-get update \  
&& apt-get install -y jq xmlstarlet  
  
# Get file and expand  
RUN curl -L http://${MIRROR}/${NIFI_BINARY_URL} -o
${NIFI_BASE_DIR}/nifi-${NIFI_VERSION}-bin.tar.gz  
RUN tar -xvzf ${NIFI_BASE_DIR}/nifi-${NIFI_VERSION}-bin.tar.gz -C
${NIFI_BASE_DIR}  
RUN rm ${NIFI_BASE_DIR}/nifi-${NIFI_VERSION}-bin.tar.gz  
  
ADD sh/ ${NIFI_BASE_DIR}/scripts/  
  
RUN chown -R nifi:nifi ${NIFI_HOME}  
USER nifi  
  
# Web HTTP(s) & Socket Site-to-Site Ports  
EXPOSE 8080 8443 10000  
  
WORKDIR ${NIFI_HOME}  
  
# Apply configuration and start NiFi  
#CMD ${NIFI_HOME}/bin/nifi.sh start  
CMD ${NIFI_BASE_DIR}/scripts/start.sh  

