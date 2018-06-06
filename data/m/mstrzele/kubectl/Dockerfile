FROM alpine:latest  
RUN wget -q -O /usr/local/bin/kubectl
https://storage.googleapis.com/kubernetes-
release/release/v1.9.1/bin/linux/amd64/kubectl && chmod +x
/usr/local/bin/kubectl  
RUN apk add --no-cache gettext  
ENTRYPOINT ["kubectl"]  

