#  
# Dockerfile for socat  
#  
FROM alpine:3.7  
  
RUN set -ex \  
&& apk add \--update socat \  
&& rm -rf /var/cache/apk  
  
ENV PORT  8388  
ENV HOST example.com  
  
EXPOSE $PORT/tcp  
EXPOSE $PORT/udp  
  
CMD socat -d -d TCP4-LISTEN:$PORT,su=nobody,fork,reuseaddr TCP4:$HOST:$PORT &
\  
socat -d -d UDP4-LISTEN:$PORT,su=nobody,fork,reuseaddr UDP4:$HOST:$PORT  

