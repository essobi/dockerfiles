FROM alpine:latest  
MAINTAINER <n3integration@gmail.com>  
  
ENV TARGET=""  
ENV DURATION="5s"  
RUN apk add curl --update --no-cache && \  
curl -fLsO
https://github.com/tsenart/vegeta/releases/download/v6.3.0/vegeta-v6.3.0-linux-
amd64.tar.gz && \  
tar -xzf vegeta-v6.3.0-linux-amd64.tar.gz && mv vegeta /usr/local/bin && \  
echo '#!/bin/sh' > /usr/bin/run-vegeta && \  
echo 'echo "GET $TARGET" | vegeta attack -duration=$DURATION | tee results.bin
| vegeta report' >> /usr/bin/run-vegeta && \  
chmod +x /usr/bin/run-vegeta && \  
rm -r /var/cache/apk  
  
CMD ["run-vegeta"]  

