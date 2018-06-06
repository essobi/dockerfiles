# Google Cloud Pub/Sub Documentation  
# https://cloud.google.com/pubsub/docs/  
FROM google/cloud-sdk:alpine  
LABEL maintainer="Cesar Perez <cesar@bigtruedata.com>" \  
version="0.1" \  
description="Google Cloud Pub/Sub Emulator"  
  
ENV PROJECT_ID=project-id \  
TOPICS="topic-1 topic-2 topic-3 topic-4 topic-5 topic-6 topic-7" \  
SUB_NAMES=TOPIC-sub \  
ACK_DEADLINE=10  
COPY rootfs /  
  
## install openjdk, copied from https://github.com/docker-
library/openjdk/blob/master/8-jre/alpine/Dockerfile  
# Default to UTF-8 file.encoding  
ENV LANG=C.UTF-8 \  
JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk/jre \  
PATH=$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin
\  
JAVA_VERSION=8u151 \  
JAVA_ALPINE_VERSION=8.151.12-r0  
  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home \  
&& set -x \  
&& apk add --no-cache \  
openjdk8-jre="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ] \  
## finish installing openjdk  
&& gcloud components install beta -q \  
&& gcloud components install pubsub-emulator -q \  
&& chmod u+x /entrypoint.sh /usr/local/bin/* \  
&& apk add --no-cache jq coreutils  
  
EXPOSE 8538  
VOLUME /data  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["gcloud", "beta", "emulators", "pubsub", "start", "--host-
port=0.0.0.0:8538", "--data-dir=/data"]  

