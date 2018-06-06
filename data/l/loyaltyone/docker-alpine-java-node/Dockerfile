FROM node:8-alpine  
  
MAINTAINER LoyaltyOne  
  
# install JRE 8 see: https://github.com/docker-
library/openjdk/blob/master/8-jre/alpine/Dockerfile  
# Default to UTF-8 file.encoding  
ENV LANG C.UTF-8  
# add a simple script that can auto-detect the appropriate JAVA_HOME value  
# based on whether the JDK or only the JRE is installed  
RUN { \  
echo '#!/bin/sh'; \  
echo 'set -e'; \  
echo; \  
echo 'dirname "$(dirname "$(readlink -f "$(which javac || which java)")")"'; \  
} > /usr/local/bin/docker-java-home \  
&& chmod +x /usr/local/bin/docker-java-home  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/jre  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
ENV JAVA_VERSION 8u131  
ENV JAVA_ALPINE_VERSION 8.131.11-r2  
  
RUN set -x \  
&& apk add --no-cache \  
openjdk8-jre="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
# install curl, bash and kms-env 0.3.0  
RUN apk upgrade --update && \  
apk add groff less python py-pip curl bash && \  
pip install awscli && \  
apk --purge -v del py-pip && \  
rm /var/cache/apk/* && \  
npm install -g kms-env@0.3.0 s3-copy@0.0.2  
  
COPY env-decrypt s3-cp /usr/local/bin/  
ENTRYPOINT ["/usr/local/bin/env-decrypt"]

