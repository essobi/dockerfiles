FROM alpine:3.7  
ARG VERSION=1.10.2  
RUN wget -q https://storage.googleapis.com/kubernetes-
release/release/v$VERSION/bin/linux/amd64/kubectl -O /usr/local/bin/kubectl &&
\  
chmod +x /usr/local/bin/kubectl && \  
apk add --no-cache --virtual .run-deps \  
ca-certificates  
ENTRYPOINT ["kubectl"]  

