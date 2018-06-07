FROM java:8-jdk-alpine  
ARG FESS_VERSION=fess-11.4.2  
RUN apk --no-cache add --virtual build-dependencies curl && \  
curl -LO
https://github.com/codelibs/fess/releases/download/${FESS_VERSION}/${FESS_VERSION}.zip
&& \  
unzip ${FESS_VERSION}.zip && \  
rm ${FESS_VERSION}.zip && \  
apk del --purge build-dependencies  
  
WORKDIR /${FESS_VERSION}  
CMD ["./bin/fess"]  

