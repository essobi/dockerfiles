FROM alpine:3.6  
MAINTAINER Marc Sensenich "hello@marc-sensenich.com"  
ENV PAPERTRAIL_API_VERSION v1  
ENV PAPERTRAIL_API_PATH systems.json  
ENV PAPERTRAIL_API_ENDPOINT
https://papertrailapp.com/api/${PAPERTRAIL_API_VERSION}/${PAPERTRAIL_API_PATH}  
ENV PAPERTRAIL_API_METHOD POST  
ENV PAPERTRAIL_API_DATA ""  
ENV PAPERTRAIL_API_TOKEN ""  
RUN apk add --no-cache \  
curl \  
ca-certificates  
  
CMD "curl" "-v" "-X" "${PAPERTRAIL_API_METHOD}" "-H" "X-Papertrail-Token:
${PAPERTRAIL_API_TOKEN}" "${PAPERTRAIL_API_ENDPOINT}" "-d"
"${PAPERTRAIL_API_DATA}"  

