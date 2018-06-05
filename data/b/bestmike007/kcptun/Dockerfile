FROM alpine:3.6  
MAINTAINER Yuanhai He <i@bestmike007.com>  
RUN apk add --no-cache curl && \  
curl -sSL https://github.com/xtaci/kcptun/releases/download/v20171201/kcptun-
linux-amd64-20171201.tar.gz | tar -C /usr/local/bin -xz && \  
mv /usr/local/bin/client_linux_amd64 /usr/local/bin/kcptun_client && \  
mv /usr/local/bin/server_linux_amd64 /usr/local/bin/kcptun_server  
  
FROM alpine:3.6  
COPY \--from=0 /usr/local/bin/kcptun_client /usr/local/bin/kcptun_client  
COPY \--from=0 /usr/local/bin/kcptun_server /usr/local/bin/kcptun_server  

