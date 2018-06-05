FROM maven:3.3.3  
MAINTAINER mmartos  
  
ENV APP_ROOT /home/tradeheader/bin  
  
COPY ./*-full.jar ${APP_ROOT}/app.jar  
  
WORKDIR ${APP_ROOT}  
  
ENTRYPOINT java -cp .:${APP_ROOT}/app.jar org.apache.camel.spring.Main

