FROM frolvlad/alpine-scala:2.11  
ENV SBT_VERSION 0.13.13  
ENV SBT_HOME /usr/share/sbt  
# Install sbt  
RUN apk add --no-cache --virtual=.build-dependencies wget ca-certificates &&
apk update && apk add libstdc++ && apk add git && \  
cd "/tmp" && \  
wget "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-${SBT_VERSION}.tgz" && \  
tar xzf "sbt-${SBT_VERSION}.tgz" && \  
mkdir -p "${SBT_HOME}" && \  
mv "/tmp/sbt-launcher-packaging-0.13.13" "/tmp/sbt/" && \  
rm "/tmp/sbt/bin/"*.bat && \  
mv "/tmp/sbt/bin" "/tmp/sbt/conf" "${SBT_HOME}" && \  
ln -s "${SBT_HOME}/bin/"* "/usr/bin/" && \  
apk del .build-dependencies && \  
rm -rf "/tmp/"*  
# prepare volume for source files and set is as working directory  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
VOLUME /usr/src/app  
  
COPY . /usr/src/app  
ENV SBT_OPTS -XX:+CMSClassUnloadingEnabled -XX:MetaspaceSize=256m
-XX:MaxMetaspaceSize=1g  
ENV LC_ALL C  
# run sbt once to load required sbt jars  
RUN sbt sbt-version compile  
RUN rm * -rf  

