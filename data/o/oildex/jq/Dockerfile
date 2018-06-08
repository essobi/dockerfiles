FROM alpine:3.7  
  
ENV JQ_VERSION=1.5-r4  
  
RUN apk add --no-cache jq=$JQ_VERSION  
  
CMD ["/usr/bin/jq", "--help"]  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.name="jq" \  
org.label-schema.version="1.5-r4" \  
org.label-schema.url="https://stedolan.github.io/jq/" \  
org.label-schema.vcs-url="https://github.com/oildex/docker-jq"  

