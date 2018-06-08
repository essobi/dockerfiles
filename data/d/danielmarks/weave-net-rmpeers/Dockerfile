FROM alpine:3.6  
RUN apk add --no-cache curl jq  
  
RUN curl -o /usr/local/bin/kubectl https://storage.googleapis.com/kubernetes-
release/release/v1.7.5/bin/linux/amd64/kubectl && chmod +x
/usr/local/bin/kubectl  
  
COPY rmpeers /  
  
RUN chmod +x /rmpeers  
  
CMD ["/rmpeers"]  

