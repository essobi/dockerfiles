FROM gliderlabs/alpine:latest  
  
RUN apk add --update curl python && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir -p /app  
WORKDIR /app  
  
ENTRYPOINT cat ${PAYLOAD_FILE} | python -c 'import
json,sys;obj=json.load(sys.stdin);print obj["args"]' | xargs curl  

