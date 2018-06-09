FROM openjdk:jre-alpine  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
DAVMAIL_VERSION=latest \  
S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \  
S6_KEEP_ENV=1 \  
S6_READ_ONLY_ROOT=1  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS \  
curl \  
&& apk add --no-cache --no-progress \  
ca-certificates \  
gettext \  
\  
# Install davmail  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/_/davmail/${DAVMAIL_VERSION}" | xargs) \  
&& curl --location
"http://downloads.sourceforge.net/project/davmail/davmail/${DAVMAIL_VERSION}/davmail-
linux-x86_64-${DAVMAIL_VERSION}-${DAVMAIL_BUILD}.tgz" | tar --directory /tmp
--extract --gzip \  
&& mkdir -p /opt \  
&& mv "/tmp/davmail-linux-x86_64-${DAVMAIL_VERSION}-${DAVMAIL_BUILD}"
/opt/davmail \  
\  
# Install timonier/dumb-entrypoint  
\  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/s6-overlay/installer" |
INSTALL_DIRECTORY="/usr/sbin" sh -s -- install \  
\  
# Clean  
\  
&& apk del --no-progress \  
BUILD_DEPS \  
&& rm -f -r \  
/tmp/*  
  
COPY ./rootfs /  
  
ENTRYPOINT [ "/init" ]  

