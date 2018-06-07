FROM openjdk:8-alpine  
  
# Install scala  
ENV SCALA_VERSION=2.12.1 \  
SCALA_HOME=/usr/share/scala  
RUN apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \  
apk add --no-cache bash && \  
cd "/tmp" && \  
wget
"https://downloads.typesafe.com/scala/${SCALA_VERSION}/scala-${SCALA_VERSION}.tgz"
&& \  
tar xzf "scala-${SCALA_VERSION}.tgz" && \  
mkdir "${SCALA_HOME}" && \  
rm "/tmp/scala-${SCALA_VERSION}/bin/"*.bat && \  
mv "/tmp/scala-${SCALA_VERSION}/bin" "/tmp/scala-${SCALA_VERSION}/lib"
"${SCALA_HOME}" && \  
ln -s "${SCALA_HOME}/bin/"* "/usr/bin/" && \  
apk del .build-dependencies && \  
rm -rf "/tmp/"*  
  
# Install sbt  
ENV SBT_VERSION 0.13.11  
ENV SBT_HOME /usr/local/sbt  
ENV PATH ${PATH}:${SBT_HOME}/bin  
RUN apk add --no-cache curl ca-certificates bash && \  
curl -sL "http://dl.bintray.com/sbt/native-
packages/sbt/$SBT_VERSION/sbt-$SBT_VERSION.tgz" | gunzip | tar -x -C
/usr/local && \  
echo -ne "- with sbt $SBT_VERSION\n" >> /root/.built &&\  
apk del curl  
  
# Load kaitai  
RUN apk add --no-cache git  
RUN git clone \--recursive https://github.com/kaitai-io/kaitai_struct.git
/kaitai  
  
# Setup kaitai  
# WORKDIR /kaitai/tests  
# RUN ./build-compiler  
# RUN ./publish-js-compiler  
# RUN ./translator-tests || true  
# RUN ./build-formats  
# RUN ./publish-targets  
# RUN ./ci-all  
# RUN ../update-ci-status  
WORKDIR /kaitai/compiler  
RUN sbt compilerJVM/universal:packageBin  
  
# ENTRYPOINT ["mysql"]  

