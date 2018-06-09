FROM alpine:3.3  
  
RUN mkdir -p /opt/scripts/  
  
RUN apk update && apk upgrade && \  
apk add \--no-cache bash nodejs  
  
RUN npm install -g stylelint  
  
COPY entrypoint.sh /opt/scripts/  
  
ENTRYPOINT ["/opt/scripts/entrypoint.sh"]  

