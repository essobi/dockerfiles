  
FROM ubuntu:16.04  
ARG BUILD_DATE  
ARG SNAP_VERSION=latest  
  
ENV SNAP_VERSION=${SNAP_VERSION}  
ENV SNAP_TRUST_LEVEL=0  
ENV SNAP_LOG_LEVEL=1  
ENV SNAP_LOG_PATH=/var/log/snap  
ENV CI_URL=https://s3-us-west-2.amazonaws.com/snap.ci.snap-telemetry.io  
  
LABEL vendor="Intelsdi-X" \  
name="Snap Ubuntu 16.04" \  
license="Apache 2.0" \  
build-date=$BUILD_DATE \  
io.snap-telemetry.snap.version=$SNAP_VERSION \  
io.snap-telemetry.snap.version.is-beta=  
  
EXPOSE 8181  
ADD ${CI_URL}/snap/${SNAP_VERSION}/linux/x86_64/snapteld
/opt/snap/sbin/snapteld  
ADD ${CI_URL}/snap/${SNAP_VERSION}/linux/x86_64/snaptel /opt/snap/bin/snaptel  
COPY init_snap /usr/local/bin/init_snap  
COPY snapteld.conf /etc/snap/snapteld.conf  
  
RUN chmod a+x /usr/local/bin/init_snap  
  
RUN /usr/local/bin/init_snap  
  
# Install CURL  
RUN apt-get update  
RUN apt-get install curl -y  
  
# Pull Kafka publisher plugin  
RUN curl -sfL "https://github.com/intelsdi-x/snap-plugin-publisher-
kafka/releases/download/9/snap-plugin-publisher-kafka_linux_x86_64" -o
/opt/snap/plugins/snap-plugin-publisher-kafka  
  
CMD /opt/snap/sbin/snapteld -t ${SNAP_TRUST_LEVEL} -l ${SNAP_LOG_LEVEL}
\--log-path ${SNAP_LOG_PATH}

