ARG JAVA_IMAGE=openjdk  
ARG JAVA_TAG=8  
FROM ${JAVA_IMAGE}:${JAVA_TAG}  
ARG GS_PRODUCT=insightedge  
ARG GS_VERSION=12.3.1  
ARG GS_MILESTONE=m7  
ARG GS_BUILD=19207  
ARG
GS_NAME=gigaspaces-${GS_PRODUCT}-open-${GS_VERSION}-${GS_MILESTONE}-b${GS_BUILD}  
ARG GS_URL=https://gigaspaces-releases-
eu.s3.amazonaws.com/${GS_PRODUCT}/${GS_VERSION}/${GS_NAME}.zip  
ENV GS_HOME /opt/gigaspaces  
# Download $GS_URL and unzip to $GS_HOME  
RUN wget \--progress=bar:force -O /tmp/gigaspaces.zip ${GS_URL} &&\  
unzip -q /tmp/gigaspaces.zip -d /tmp && \  
mv /tmp/${GS_NAME} ${GS_HOME} && \  
rm -f /tmp/gigaspaces.zip  
WORKDIR ${GS_HOME}  
ADD entrypoint.sh /opt/entrypoint.sh  
# Configure and expose ports  
ENV XAP_NIC_ADDRESS "#eth0:ip#"  
ENV XAP_LOOKUP_PORT 4174  
ENV XAP_LRMI_PORT 8200-8300  
ENV SPARK_MASTER_PORT 7077  
ENV SPARK_MASTER_WEBUI_PORT 8080  
ENV ZEPPELIN_PORT 9090  
EXPOSE ${XAP_LOOKUP_PORT} ${XAP_LRMI_PORT} ${SPARK_MASTER_PORT}
${SPARK_MASTER_WEBUI_PORT} ${ZEPPELIN_PORT}  
ENV EXT_JAVA_OPTIONS "-Dcom.gs.multicast.discoveryPort=${XAP_LOOKUP_PORT}
-Dcom.gs.transport_protocol.lrmi.bind-port=${XAP_LRMI_PORT}"  
ENTRYPOINT ["/opt/entrypoint.sh"]  
CMD ["demo"]

