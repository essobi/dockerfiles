FROM paulbrown/base:latest  
  
ENV KAFKA_USER=kafka \  
KAFKA_HOME=/kafka \  
KAFKA_DATA_DIR=/kafka_data \  
KAFKA_LOG_DIR=/kafka_log  
  
ARG KAFKA_VERSION=0.11.0.0  
ARG KAFKA_DIST=kafka_2.11-0.11.0.0  
RUN set -x pipefail \  
&& yum update --assumeyes \  
&& yum install --assumeyes java-1.8.0-openjdk-headless wget \  
&& wget --quiet
"http://www.apache.org/dist/kafka/$KAFKA_VERSION/$KAFKA_DIST.tgz" \  
&& wget --quiet
"http://www.apache.org/dist/kafka/$KAFKA_VERSION/$KAFKA_DIST.tgz.asc" \  
&& wget --quiet "http://www.apache.org/dist/kafka/KEYS" \  
&& export GNUPGHOME="$(mktemp --directory)" \  
&& gpg --import KEYS \  
&& gpg --batch --verify "$KAFKA_DIST.tgz.asc" "$KAFKA_DIST.tgz" \  
&& tar --extract --ungzip --file="$KAFKA_DIST.tgz" \--directory=/opt \  
&& rm --recursive --force "$GNUPGHOME" "$KAFKA_DIST.tgz" "$KAFKA_DIST.tgz.asc"
\  
&& rm --recursive --force /opt/$KAFKA_DIST/NOTICE \  
/opt/$KAFKA_DIST/site-docs \  
&& yum erase --assumeyes wget \  
&& yum clean all  
  
# Copy configuration generator and setup scripts to bin and make executable  
COPY kafkaGenConfig.sh "/opt/$KAFKA_DIST/bin/"  
  
# Create a user for the kafka process and configure file system ownership  
# for nessecary directories and modify scripts as a user executable  
RUN set -x pipefail \  
&& mkdir --parents $KAFKA_DATA_DIR $KAFKA_LOG_DIR \  
&& groupadd --gid 1000 $KAFKA_USER \  
&& useradd --uid 1000 --gid $KAFKA_USER \--home $KAFKA_HOME $KAFKA_USER \  
&& ln -s -t $KAFKA_HOME /opt/$KAFKA_DIST/* $KAFKA_DATA_DIR $KAFKA_LOG_DIR \  
&& chown -R -L "$KAFKA_USER:$KAFKA_USER" $KAFKA_HOME \  
&& chmod +x "$KAFKA_HOME/bin/kafkaGenConfig.sh"  
  
# Set working directory to kafka home  
WORKDIR $KAFKA_HOME  
  
# Set non-root user on container start  
USER 1000

