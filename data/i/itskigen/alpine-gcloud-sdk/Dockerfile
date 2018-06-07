FROM alpine:3.6  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="alpine-gcloud-sdk" \  
org.label-schema.description="gcloud SDK Image based on Alpine distro" \  
org.label-schema.url="https://www.254bit.com/" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/kigen/alpine-gcloud-sdk" \  
org.label-schema.vendor="254Bit" \  
org.label-schema.version=$VERSION \  
org.label-schema.schema-version="0.1.0"  
  
############ JAVA 8 #############################  
  
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
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
  
ENV JAVA_VERSION 8u131  
ENV JAVA_ALPINE_VERSION 8.131.11-r2  
  
RUN set -x \  
&& apk add --no-cache \  
openjdk8="$JAVA_ALPINE_VERSION" \  
&& [ "$JAVA_HOME" = "$(docker-java-home)" ]  
  
############ GOOGLE CLOUD SDK #############################  
  
ENV HOME=/\  
CLOUDSDK_PYTHON_SITEPACKAGES=1\  
PATH=/google-cloud-sdk/bin:$PATH  
  
RUN echo "ipv6" >> /etc/modules  
  
RUN set -x\  
#&& echo "http://dl-5.alpinelinux.org/alpine/v3.6/main" >
/etc/apk/repositories\  
&& apk update\  
&& apk --no-cache add --virtual .build-deps\  
ca-certificates\  
unzip\  
wget\  
&& apk --no-cache add\  
bash\  
openssh-client\  
php5-cgi\  
php5-cli\  
php5-mysql\  
git\  
openssh\  
#&& echo "http://nl.alpinelinux.org/alpine/v3.6/main" > /etc/apk/repositories\  
#&& apk update\  
#&& apk --no-cache add --virtual .build-deps\  
py2-openssl\  
python2\  
&& wget https://dl.google.com/dl/cloudsdk/channels/rapid/google-cloud-sdk.zip\  
&& unzip google-cloud-sdk.zip\  
&& rm google-cloud-sdk.zip\  
&& google-cloud-sdk/install.sh\  
\--usage-reporting=true\  
\--path-update=true\  
\--bash-completion=true\  
\--rc-path=/.bashrc\  
\--additional-components\  
alpha\  
app-engine-go\  
app-engine-java\  
app-engine-python\  
beta\  
bigtable\  
bq\  
cloud-datastore-emulator\  
docker-credential-gcr\  
gcd-emulator\  
gsutil\  
kubectl\  
pubsub-emulator\  
&& apk del .build-deps\  
&& rm -rf /var/cache/apk/*\  
&& google-cloud-sdk/bin/gcloud config set --installation
component_manager/disable_update_check true\  
&& sed -i -- 's/\"disable_updater\": false/\"disable_updater\": true/g'
/google-cloud-sdk/lib/googlecloudsdk/core/config.json\  
&& mkdir /.ssh  
  
VOLUME ["/.config"]

