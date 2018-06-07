FROM alpine:3.5  
ARG LIBSASS_VERSION=3.4.3  
ARG SASSC_VERSION=3.4.2  
ENV SASS_LIBSASS_PATH "/usr/local/libsass"  
RUN apk add --no-cache libstdc++  
  
# Compile and install SassC, without dependency bulk  
RUN apk add --no-cache --virtual build-dependencies \  
build-base \  
ca-certificates \  
openssl \  
unzip \  
&& update-ca-certificates \  
&& mkdir -p /usr/local /data \  
&& cd /usr/local \  
&& wget -O libsass.zip
"https://github.com/sass/libsass/archive/${LIBSASS_VERSION}.zip" \  
&& wget -O sassc.zip
"https://github.com/sass/sassc/archive/${SASSC_VERSION}.zip" \  
&& unzip libsass.zip \  
&& unzip sassc.zip \  
&& mv "sassc-${SASSC_VERSION}" sassc \  
&& mv "libsass-${LIBSASS_VERSION}" libsass \  
&& cd "/usr/local/sassc" \  
&& make \  
&& ln -s /usr/local/sassc/bin/sassc /usr/local/bin/sassc \  
&& rm -fr /usr/local/*.zip \  
&& apk del build-dependencies  
  
# Run SassC by default  
ENTRYPOINT ["sassc"]  
VOLUME /data  
WORKDIR /data  

