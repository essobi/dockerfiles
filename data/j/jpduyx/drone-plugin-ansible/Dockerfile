FROM alpine:edge  
  
LABEL Maintainer="Jean-Paul Duyx | github.com/jpduyx" \  
Description="Lightweight ansible container as drone.io plugin with
apache_libcloud based on Alpine Linux."  
  
# Install packages  
RUN apk update && \  
apk --no-cache add openssh-client ansible sshpass py-pip && \  
pip install --upgrade pip apache_libcloud && \  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/*  
  
ENV PATH /usr/sbin:$PATH  
  
CMD ["ansible", "--version"]  

