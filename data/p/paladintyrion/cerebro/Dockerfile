FROM openjdk:8-jdk-alpine  
MAINTAINER paladintyrion <paladintyrion@gmail>  
  
ENV CEREBRO_VERSION 0.7.1  
ENV CEREBRO_HOME /opt/cerebro  
ENV URL "https://github.com/lmenezes/cerebro/releases/download"  
ENV TARBALL "$URL/v${CEREBRO_VERSION}/cerebro-${CEREBRO_VERSION}.tgz"  
RUN apk update \  
&& apk add --no-cache bash \  
&& apk add --no-cache -t .build-deps wget openssl tar \  
&& cd /tmp \  
&& wget --no-check-certificate --progress=bar:force -O cerebro.tgz "$TARBALL"
\  
&& mkdir -p "$CEREBRO_HOME" \  
&& tar -zxf cerebro.tgz --strip-components=1 -C "$CEREBRO_HOME" \  
&& rm -f cerebro.tgz \  
&& apk del --purge .build-deps \  
&& rm -fr /tmp/*  
  
ENV PATH $CEREBRO_HOME/bin:$PATH  
  
EXPOSE 9494  
ENTRYPOINT ["cerebro"]  
  
CMD ["-Dhttp.port=9494", "-Dhttp.address=0.0.0.0"]  

