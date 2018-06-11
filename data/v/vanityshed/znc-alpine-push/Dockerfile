FROM alpine:3.6  
MAINTAINER Stevesbrain  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="stevesbrain version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
ENV GPG_KEY D5823CACB477191CAC0075555AE420CC0209989E  
# package version  
ARG CONFIGUREFLAGS="--prefix=/opt/znc --enable-cyrus --enable-perl --enable-
python --disable-ipv6"  
ARG MAKEFLAGS="-j"  
ENV ZNC_VERSION 1.6.5  
#Cleaning house  
COPY clean_py.sh /  
# Build ZNC  
RUN set -x \  
&& apk add --no-cache --virtual runtime-dependencies \  
ca-certificates \  
cyrus-sasl \  
icu \  
openssl \  
tini \  
py3-requests \  
git \  
tzdata \  
&& apk add --no-cache --virtual build-dependencies \  
build-base \  
curl \  
cyrus-sasl-dev \  
gnupg \  
icu-dev \  
openssl-dev \  
perl-dev \  
python3-dev \  
&& mkdir /znc-src && cd /znc-src \  
&& curl -fsSL "http://znc.in/releases/archive/znc-${ZNC_VERSION}.tar.gz" -o
znc.tgz \  
&& curl -fsSL "http://znc.in/releases/archive/znc-${ZNC_VERSION}.tar.gz.sig"
-o znc.tgz.sig \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& curl
https://gist.githubusercontent.com/stevesbrain/e0cb404d3a31fde8cd23a36fadebe2e8/raw/bc06cd01785b371b3beb3408ff1b25fdecbcbe48/DarthGandalfKey.asc
| gpg --import \  
&& gpg --batch --verify znc.tgz.sig znc.tgz \  
&& rm -rf "$GNUPGHOME" \  
&& tar -zxf znc.tgz --strip-components=1 \  
&& PYTHONDONTWRITEBYTECODE=yes \  
&& mkdir build && cd build \  
&& ../configure ${CONFIGUREFLAGS} \  
&& make $MAKEFLAGS \  
&& make install \  
&& rm -rf /src \  
&& apk del --purge build-dependencies \  
&& rm -rf /znc-src; exit 0  
  
# Build the ZNC modules  
RUN set -x \  
&& mkdir /docker \  
&& apk add --no-cache --virtual build-dependencies \  
build-base \  
icu-dev \  
openssl-dev \  
curl \  
&& cd /docker \  
&& git clone https://github.com/jreese/znc-push.git \  
&& cd /docker/znc-push \  
&& PATH=$PATH:/opt/znc/bin \  
&& make \  
&& mkdir -p /docker/modules \  
&& cp /docker/znc-push/push.so /docker/modules/ \  
&& cd /docker \  
&& git clone https://github.com/moshee/modignore \  
&& cd /docker/modignore \  
&& znc-buildmod ignore.cc \  
&& cp ignore.so /docker/modules/ \  
&& cd /docker \  
&& mkdir /docker/simple_disconnect \  
&& cd /docker/simple_disconnect \  
&& curl -fsSL
https://gist.githubusercontent.com/maxpowa/57e5d6fb3afb944671f5/raw/8158ec1e4325c5d04078ff77143f7ca5bdd8ed67/simple_disconnect.cpp
-o simple_disconnect.cpp \  
&& znc-buildmod simple_disconnect.cpp \  
&& cp /docker/simple_disconnect/simple_disconnect.so /docker/modules/ \  
&& cd /docker \  
&& rm -rf /docker/znc-push \  
&& rm -rf /docker/modignore \  
&& rm -rf /src \  
&& apk del --purge build-dependencies build-base curl \  
&& /clean_py.sh; exit 0  
  
# Add our users for ZNC  
RUN adduser -u 1000 -S znc  
RUN addgroup -g 1000 -S znc  
  
#Make the ZNC Data dir  
RUN mkdir /znc-data  
  
#Copy the necessary files  
WORKDIR /  
COPY docker-entrypoint.sh /  
COPY znc.conf.example /docker  
  
#Change ownership as needed  
RUN chown -R znc:znc /znc-data  
RUN chown -R znc:znc /docker  
  
#The user that we enter the container as, and that everything runs as  
USER znc  
VOLUME /znc-data  
ENV BUILD 0.3.6  
ENTRYPOINT ["/docker-entrypoint.sh"]  

