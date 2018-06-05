# build stage  
FROM alpine:3.7 as build  
  
ARG WRK_VERSION=4.0.2  
RUN apk add --no-cache --virtual .build-deps \  
build-base \  
perl \  
&& wget -O /tmp/wrk.tar.gz
https://github.com/wg/wrk/archive/${WRK_VERSION}.tar.gz \  
&& tar -xzf /tmp/wrk.tar.gz -C /tmp/ \  
&& make -C /tmp/wrk-${WRK_VERSION} \  
&& mv /tmp/wrk-${WRK_VERSION}/wrk /wrk  
  
# upx stage  
FROM gruebel/upx:latest as upx  
  
COPY \--from=build /wrk /wrk.org  
  
RUN upx --best --lzma -o /wrk /wrk.org  
  
# final stage  
FROM alpine:3.7  
ARG BUILD_DATE  
  
LABEL org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.schema-version="1.0"  
  
RUN apk add --no-cache \  
libgcc  
  
COPY \--from=upx /wrk /usr/bin/wrk  
  
ENTRYPOINT ["wrk"]  

