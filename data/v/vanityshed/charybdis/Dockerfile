FROM alpine:3.7  
MAINTAINER Stevesbrain  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="stevesbrain version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
ARG CONFIGUREFLAGS="--enable-openssl --prefix=/irc"  
ENV CHARYBDIS_RELEASE 3.5.5  
# Build Charybdis  
RUN set -x \  
&& apk add --no-cache --virtual runtime-dependencies \  
openssl \  
openssl-dev \  
build-base \  
curl \  
bison \  
flex \  
&& mkdir /charybdis-src && cd /charybdis-src \  
&& curl -fsSL "https://github.com/charybdis-
ircd/charybdis/archive/charybdis-${CHARYBDIS_RELEASE}.tar.gz" -o
charybdis.tar.gz \  
&& tar -zxf charybdis.tar.gz --strip-components=1 \  
&& mkdir /irc \  
&& ./configure ${CONFIGUREFLAGS} \  
&& make \  
&& make install \  
&& apk del --purge build-dependencies \  
openssl-dev \  
&& cd /root \  
&& rm -rf /charybdis-src \  
&& rm -rf /src; exit 0  
  
# Add our users for charybdis  
RUN adduser -u 1000 -S ircd  
RUN addgroup -g 1000 -S ircd  
  
#Change ownership as needed  
RUN chown -R ircd:ircd /irc  
#The user that we enter the container as, and that everything runs as  
USER ircd  
ENV BUILD 0.2.0  
ENTRYPOINT ["/irc/bin/ircd", "-pidfile", "/irc/ircd.pid", "-foreground"]  

