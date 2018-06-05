ARG BUILD_FROM=resin/i386-alpine:3.6  
FROM $BUILD_FROM  
  
ENV GPG_KEY D5823CACB477191CAC0075555AE420CC0209989E  
  
# modperl and modpython are built, but won't be loadable.  
# :full image installs perl and python3 again, making these modules loadable.  
# musl silently doesn't support AI_ADDRCONFIG yet, and ZNC doesn't support
Happy Eyeballs yet.  
# Together they cause very slow connection. So for now IPv6 is disabled here.  
ARG CONFIGUREFLAGS="--prefix=/opt/znc --enable-cyrus --enable-perl --enable-
python --disable-ipv6"  
ARG MAKEFLAGS=""  
  
ENV ZNC_VERSION 1.6.5  
  
  
  
RUN set -x \  
&& adduser -S znc \  
&& addgroup -S znc \  
&& apk add --no-cache --virtual runtime-dependencies \  
znc \  
znc-extra \  
znc-modpython \  
znc-modperl \  
znc-doc \  
ca-certificates \  
cyrus-sasl \  
icu \  
su-exec \  
tini \  
tzdata \  
&& apk add --no-cache --virtual build-dependencies \  
znc-dev \  
build-base \  
curl \  
cyrus-sasl-dev \  
gnupg \  
icu-dev \  
libressl-dev \  
perl-dev \  
python3-dev  
  
  
  
COPY src/ /  
  
VOLUME /data  
EXPOSE 1337  
  
ENTRYPOINT ["/entrypoint.sh"]  

