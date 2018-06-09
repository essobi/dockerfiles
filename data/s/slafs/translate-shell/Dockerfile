FROM alpine:latest  
  
RUN apk add --no-cache curl bash ca-certificates less gawk  
  
ADD http://git.io/trans /usr/local/bin/trans  
  
RUN chmod +x /usr/local/bin/trans  
  
ENTRYPOINT ["/usr/local/bin/trans"]  
  

