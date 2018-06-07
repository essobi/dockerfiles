FROM frolvlad/alpine-oraclejdk8:slim  
MAINTAINER Bryan Talbot <bryan.talbot@ijji.com>  
EXPOSE 9324  
ENV ELASTICMQ_VERSION=0.8.12 \  
ELASTICMQ_SHA256=807fb1657f4cde2f4b9373a87c7b30dfa4a590682935f944ac3be78449b33a53  
  
WORKDIR /elasticmq  
  
# Download and install the binaries to WORKDIR  
RUN wget -q -O elasticmq-server.jar http://s3-eu-
west-1.amazonaws.com/softwaremill-public/elasticmq-
server-${ELASTICMQ_VERSION}.jar && \  
echo "${ELASTICMQ_SHA256} elasticmq-server.jar" | sha256sum -c -  
  
ENV ELASTICMQ_OPTS=""  
CMD exec java ${ELASTICMQ_OPTS} -jar elasticmq-server.jar  

