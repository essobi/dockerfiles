FROM alpine:latest  
  
RUN apk add --no-cache bash jq httpie  
  
COPY run.sh /scripts/run.sh  
  
ENTRYPOINT ["/bin/bash", "/scripts/run.sh"]  

