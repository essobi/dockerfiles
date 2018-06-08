FROM alpine as builder  
  
RUN apk add --no-cache wget tar ca-certificates \  
&& wget -q https://github.com/magi-
project/magi/releases/download/v1.4.4.1/m-wallet-1.4.4.1-linux.tar.gz \  
&& tar xvf m-wallet-1.4.4.1-linux.tar.gz \  
&& mv m-wallet-1.4.4.1-linux/bin/64/magid / \  
&& rm -r m-wallet-1.4.4.1-linux  
  
FROM ubuntu  
  
COPY \--from=builder /magid /magid  
  
VOLUME ["/root/.magi/magi.conf"]  
VOLUME ["/root/.magi/blocks"]  
VOLUME ["/root/.magi/database"]  
  
ENTRYPOINT ["/magid"]

