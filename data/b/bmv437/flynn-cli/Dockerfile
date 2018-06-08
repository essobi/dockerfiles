FROM alpine  
  
RUN apk add --no-cache curl git  
  
RUN L=/usr/local/bin/flynn && curl -sSL -A "`uname -sp`"
https://dl.flynn.io/cli | zcat >$L && chmod +x $L  

