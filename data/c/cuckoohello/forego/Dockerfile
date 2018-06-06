FROM alpine  
RUN apk add --update --no-cache tzdata && cp /usr/share/zoneinfo/Asia/Shanghai
/etc/localtime && echo "Asia/Shanghai" > /etc/timezone && apk del tzdata  
  
RUN apk add --update curl su-exec bash && curl -fsSL
https://bin.equinox.io/c/ekMN3bCZFUn/forego-stable-linux-amd64.tgz | tar xzv
-C /usr/local/bin && chmod +x /usr/local/bin/forego  

