FROM alpine  
  
RUN apk add --no-cache ca-certificates  
  
COPY pproxies-alpine /bin/pproxies  
  
ENV PORT 9527  
ENV CHUNK_SIZE 5  
ENV TEST_URL http://httpbin.org/ip  
ENV PROXY_TIMEOUT 5  
ENV TEST_TIMEOUT 5  
ENV MAX_ERROR 15  
ENV PROXY_NUM 5  
ENV INTERVAL 5  
ENV API default  
  
EXPOSE $PORT  
  
CMD /bin/pproxies -p $PORT -s $CHUNK_SIZE -u $TEST_URL -t $PROXY_TIMEOUT -T
$TEST_TIMEOUT -e $MAX_ERROR -n $PROXY_NUM \--interval $INTERVAL \--api $API  

