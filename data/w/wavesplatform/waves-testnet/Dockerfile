FROM anapsix/alpine-java:8_server-jre  
  
MAINTAINER Alexey Kiselev <alexey.kiselev@gmail.com>  
  
EXPOSE 6869 6868  
ENV WAVES_VERSION v0.3.3  
RUN mkdir /build /waves  
  
VOLUME ["/waves"]  
  
WORKDIR /build  
  
RUN apk add --no-cache curl git bc perl openssl  
  
RUN git clone https://github.com/grondilu/bitcoin-bash-tools.git  
  
RUN curl -sL
"https://github.com/wavesplatform/Waves/releases/download/${WAVES_VERSION}/waves-${WAVES_VERSION}-testnet-
jar.tgz" | gunzip | tar -x  
  
ADD docker-entrypoint.sh /build/docker-entrypoint.sh  
  
RUN chmod -v +x docker-entrypoint.sh  
  
ENTRYPOINT /build/docker-entrypoint.sh  

