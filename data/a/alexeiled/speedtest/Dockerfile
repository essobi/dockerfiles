FROM alpine:3.4  
  
MAINTAINER Alexei Ledenev <alexei.led@gmail.com>  
  
RUN apk update \--no-cache && \  
apk add \--no-cache python && \  
apk add \--virtual .curl_ssl curl ca-certificates && \  
curl -sLo /usr/local/bin/speedtest-cli
https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py && \  
chmod +x /usr/local/bin/speedtest-cli && \  
apk del .curl_ssl  
  
ENTRYPOINT ["/usr/local/bin/speedtest-cli"]  
  

