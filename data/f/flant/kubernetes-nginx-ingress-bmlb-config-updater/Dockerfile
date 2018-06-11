FROM alpine:3.6  
MAINTAINER Dmitry Stolyarov <dmitry.stolyarov@flant.com>  
  
ADD https://storage.googleapis.com/kubernetes-
release/release/v1.6.9/bin/linux/amd64/kubectl /usr/bin/kubectl  
  
CMD ["/usr/bin/bmlb-config-updater"]  
  
RUN apk update && apk add bash && chmod +x /usr/bin/kubectl  
  
COPY rootfs /  

