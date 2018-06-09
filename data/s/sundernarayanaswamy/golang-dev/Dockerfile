FROM golang:alpine  
  
RUN apk --no-cache update && \  
apk --no-cache add bash bash-doc bash-completion curl emacs git && \  
rm -rf /var/cache/apk/*  
  
WORKDIR /home  
  
ENV GOPATH /home/go  
ENV GOROOT /usr/local/go  
  
CMD /bin/bash  

