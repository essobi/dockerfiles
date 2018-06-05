FROM project42/s6-alpine:3.6  
MAINTAINER Jordan Clark jordan.clark@esu10.org  
  
  
  
RUN apk add --no-cache nfs-utils rpcbind  
  
COPY container-files /  
  
ENTRYPOINT ["/init"]  

