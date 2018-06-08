FROM kamikat/shadowsocks-libev:2.5.6-alpine  
  
ENV LOCAL_PORT=1080  
ENV INTERVAL=3600  
ENV TEST_URL=http://ifconfig.co  
ENV EXTRA_CURL=  
  
USER root  
  
RUN apk add --no-cache curl && rm -rf /tmp/*  
  
USER nobody  
  
CMD (ss-local -s $SERVER_ADDR \  
-p $SERVER_PORT \  
-k ${PASSWORD:-$(hostname)} \  
-l $LOCAL_PORT \  
-m $METHOD \  
-t $TIMEOUT \  
--fast-open -u \  
$EXTRA_FLAGS &); \  
sleep 3; \  
while true; do curl -s \  
--socks5-hostname 127.0.0.1:$LOCAL_PORT \  
"$TEST_URL" $EXTRA_CURL; \  
sleep $INTERVAL; \  
done  

