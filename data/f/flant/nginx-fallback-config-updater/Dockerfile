FROM alpine:3.6  
MAINTAINER Andrey Klimentyev <andrey.klimentyev@flant.com>  
  
ADD https://storage.googleapis.com/kubernetes-
release/release/v1.7.5/bin/linux/amd64/kubectl /usr/bin/kubectl  
  
CMD ["/usr/bin/config-updater"]  
  
RUN apk update && apk add bash && chmod +x /usr/bin/kubectl  
  
COPY rootfs /  

