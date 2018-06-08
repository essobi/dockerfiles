FROM alpine  
  
COPY root /  
  
RUN adduser -S -D -H -h /xmrig-proxy xmrig && \  
apk update && \  
apk upgrade && \  
apk add --no-cache libuv libmicrohttpd util-linux && \  
rm -rf /var/cache/apk/*  
  
USER xmrig  
  
WORKDIR /xmrig-proxy  
  
ENTRYPOINT [ "./xmrig-proxy" ]  
CMD [ "--help" ]  

