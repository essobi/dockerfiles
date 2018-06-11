FROM anapsix/alpine-java:8_server-jre  
  
MAINTAINER Alexey Kiselev <alexey.kiselev@gmail.com>  
  
EXPOSE 6863 6869  
ENV SCALA_VERSION 2.11.8  
ENV SBT_VERSION 0.13.12  
RUN mkdir /build /waves  
  
VOLUME ["/waves"]  
  
WORKDIR /build  
  
RUN apk add --no-cache curl git bc perl openssl  
  
RUN curl -sL
"http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz"
| gunzip | tar -x  
  
RUN curl -sL "https://dl.bintray.com/sbt/native-
packages/sbt/${SBT_VERSION}/sbt-${SBT_VERSION}.tgz" | gunzip | tar -x  
  
RUN sbt/bin/sbt sbtVersion  
  
RUN git clone https://github.com/grondilu/bitcoin-bash-tools.git  
  
RUN git clone https://github.com/wavesplatform/Scorex.git  
  
RUN git clone https://github.com/wavesplatform/Waves.git  
  
WORKDIR /build/Waves  
  
RUN /build/sbt/bin/sbt update  
  
WORKDIR /build  
  
ADD docker-entrypoint.sh /build/docker-entrypoint.sh  
  
RUN chmod -v +x docker-entrypoint.sh  
  
ENTRYPOINT ["/build/docker-entrypoint.sh"]  

