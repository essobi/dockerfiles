FROM alpine:3.5  
RUN apk --no-cache update && \  
apk --no-cache add ca-certificates curl && \  
rm -rf /var/cache/apk/*  
RUN curl -L https://storage.googleapis.com/kubernetes-
release/release/v1.7.11/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \  
&& chmod +x /usr/local/bin/kubectl  
ENTRYPOINT ["/usr/local/bin/kubectl"]  

