FROM golang:1.10-alpine AS build  
  
WORKDIR /go/src/proxy  
COPY proxy.go proxy.go  
RUN apk add \--no-cache git && go get  
FROM alpine:3.7  
  
RUN \  
apk add \--no-cache \  
su-exec \  
tzdata  
  
COPY \--from=build /go/bin/proxy /usr/local/bin/proxy  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
ENV \  
USER_UID=1000 \  
USER_GID=1000 \  
\  
CLICKHOUSE_ADDR= \  
PROXY_PERIOD=60 \  
PROXY_BATCH=10000  
  
EXPOSE 9001  
  
CMD ["/usr/local/bin/entrypoint.sh"]  

