FROM openjdk:8u151-jdk-alpine  
  
  
ENV LANG=C.UTF-8  
ENV LC_ALL=C.UTF-8  
ENV WM_VERSION=2.17.0  
ENV
WM_STANDALONE_URL=https://repo1.maven.org/maven2/com/github/tomakehurst/wiremock-
standalone/$WM_VERSION/wiremock-standalone-$WM_VERSION.jar  
ENV WM_BODY_TRANSFORMER=https://github.com/opentable/wiremock-body-
transformer/releases/download/wiremock-body-transformer-1.1.6/wiremock-body-
transformer-1.1.6.jar  
  
ENV XMS=512m  
ENV XMX=512m  
ENV JAVA_OPTS=" -server -XX:+AggressiveOpts -Xms${XMS} -Xmx${XMX} "  
  
ENV CMD_PORT=80  
ENV CMD_HTTPS_PORT=443  
ENV CMD_CONTAINER_THREADS=10  
ENV CMD_PRINT_ALL_NETWORK_TRAFFIC=true  
ENV CMD_PORT=80  
ENV CMD_PROXY_TARGET=""  
ADD $WM_STANDALONE_URL /wiremock/wiremock.jar  
ADD $WM_BODY_TRANSFORMER /wiremock/wiremock-body-transformer.jar  
  
WORKDIR /wiremock  
  
EXPOSE 80 443  
  
COPY ./entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  

