FROM openjdk:8-jre-alpine  
  
RUN apk --no-cache add bash  
RUN apk --no-cache add curl  
  
ENV CEREBRO_VERSION 0.7.1  
RUN curl --progress-bar -L
"https://github.com/lmenezes/cerebro/releases/download/v${CEREBRO_VERSION}/cerebro-${CEREBRO_VERSION}.tgz"
| tar zx \  
&& mv cerebro-${CEREBRO_VERSION} cerebro  
  
RUN apk del curl  
  
RUN rm -rf /var/cache/apk/*  
  
RUN sed -i '/<appender-ref ref="FILE"\/>/d' cerebro/conf/logback.xml  
  
WORKDIR /cerebro  
EXPOSE 9000  
ENTRYPOINT ["./bin/cerebro"]  

