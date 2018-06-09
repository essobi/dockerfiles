FROM supersoftware/rancher-cli:0.6.4  
ENV BUILD_PACKAGES build-base git autoconf automake  
  
RUN apk update && \  
apk upgrade && \  
apk add git tar && \  
rm -rf /var/cache/apk/*  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

