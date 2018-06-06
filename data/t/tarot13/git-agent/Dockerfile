FROM alpine  
  
LABEL maintainer "Ian Li <OpenSource@ianli.xyz>"  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN apk add --no-cache ca-certificates bash git nano wget curl && \  
update-ca-certificates && \  
chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]

