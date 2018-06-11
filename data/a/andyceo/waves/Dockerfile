FROM alpine as crawler  
ENV WAVES_VERSION 0.9.2  
RUN apk add --no-cache --update ca-certificates curl && \  
update-ca-certificates && \  
curl -sLo /waves.jar
"https://github.com/wavesplatform/Waves/releases/download/v${WAVES_VERSION}/waves-
all-${WAVES_VERSION}.jar" && \  
curl -sLo /waves-devnet.conf
"https://raw.githubusercontent.com/wavesplatform/Waves/v${WAVES_VERSION}/waves-
devnet.conf" && \  
curl -sLo /waves-mainnet.conf
"https://raw.githubusercontent.com/wavesplatform/Waves/v${WAVES_VERSION}/waves-
mainnet.conf" && \  
curl -sLo /waves-testnet.conf
"https://raw.githubusercontent.com/wavesplatform/Waves/v${WAVES_VERSION}/waves-
testnet.conf"  
  
FROM openjdk:9-jre-slim  
MAINTAINER Andrey Andreev <andyceo@yandex.ru> (@andyceo)  
COPY \--from=crawler /waves.jar /waves.jar  
COPY \--from=crawler /waves-devnet.conf /waves-devnet.conf  
COPY \--from=crawler /waves-mainnet.conf /waves-mainnet.conf  
COPY \--from=crawler /waves-testnet.conf /waves-testnet.conf  
EXPOSE 6869 6868  
VOLUME ["/root/waves"]  
ENTRYPOINT ["/usr/bin/java", "-jar", "/waves.jar"]  
CMD ["/waves-mainnet.conf"]  

