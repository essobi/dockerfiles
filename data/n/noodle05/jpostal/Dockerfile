FROM openjdk:8-jre-alpine  
  
MAINTAINER Wei Gao<wei@gaofmaily.org>  
  
ENV LIBPOSTAL_DATA=/data  
  
RUN \  
# Install required packages \  
apk add \--no-cache snappy curl bash findutils tar coreutils \  
# Install dependencies, will remove later \  
&& apk add \--no-cache \--virtual .build-deps snappy-dev \  
git autoconf automake make gcc libtool libc-dev \  
openjdk8 \  
&& mkdir -p /tmp/src \  
&& cd /tmp/src \  
# Build libpostal first \  
&& git clone https://github.com/openvenues/libpostal.git \  
&& cd libpostal \  
# Fix some libpostal build time warnings \  
&& echo "ACLOCAL_AMFLAGS = -I m4" >> Makefile.am \  
&& echo "AC_CONFIG_MACRO_DIR([m4])" >> configure.ac \  
&& mkdir m4 \  
# This docker image will not download data \  
&& sed -i -e
's/\(\s*.*\/libpostal_data\s*download\s*all\s*\$(datadir)\/libpostal\\)/#\1/g'
src/Makefile.am \  
&& ./bootstrap.sh \  
# Since this is delegated to libpostal, use "/usr" as prefix \  
&& ./configure \--prefix=/usr \--datadir=/data \  
&& make -j \  
&& make install \  
&& cd /tmp/src \  
# Build libpostal java API \  
&& git clone https://github.com/openvenues/jpostal.git \  
&& cd jpostal \  
# Use "/usr" as prefix \  
&& sed -i -e 's/\--libdir=\$(pwd)\/src\/main\/jniLibs/--prefix=\/usr/g'
build.sh \  
&& sed -i -e 's/make install/make -j install/g' build.sh \  
&& export JAVA_HOME=/usr/lib/jvm/default-jvm \  
&& export PATH=$PATH:$JAVA_HOME/bin \  
&& /tmp/src/jpostal/gradlew assemble \  
&& cp /tmp/src/jpostal/build/libs/jpostal.jar /usr/lib/jvm/default-
jvm/jre/lib/ext/ \  
&& cd / \  
&& apk del .build-deps \  
&& rm -fr .build-deps /tmp/src /tmp/hsperfdata_root /root/.gradle
/root/.ash_history  
  
ADD docker-entrypoint.sh /  
  
VOLUME [ "/data" ]  
  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  

