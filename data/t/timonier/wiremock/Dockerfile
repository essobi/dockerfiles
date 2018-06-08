FROM openjdk:jre-alpine  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
WIREMOCK_VERSION=latest  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add \--no-cache --no-progress --virtual BUILD_DEPS \  
curl \  
\  
# Install timonier/dumb-entrypoint  
\  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/dumb-entrypoint/installer" |
INSTALL_DIRECTORY="/usr/sbin" sh -s -- install \  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/gosu/installer" | INSTALL_DIRECTORY="/usr/sbin" sh
-s -- install \  
\  
# Install wiremock  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/tomakehurst/wiremock/${WIREMOCK_VERSION}" | xargs) \  
&& mkdir -p /opt/wiremock \  
&& curl --location --output /opt/wiremock/wiremock.jar
"http://repo1.maven.org/maven2/com/github/tomakehurst/wiremock-
standalone/${WIREMOCK_VERSION}/wiremock-standalone-${WIREMOCK_VERSION}.jar" \  
\  
# Clean  
\  
&& apk del --no-progress \  
BUILD_DEPS  
  
COPY ./rootfs /  
  
ENTRYPOINT [ "dumb-entrypoint" ]  

