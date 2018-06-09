FROM golang:alpine  
  
RUN apk update && \  
apk add alpine-sdk  
  
COPY . $GOPATH/src/gitlab.com/novacloud/wab  
  
WORKDIR $GOPATH/src/gitlab.com/novacloud/wab  
  
RUN make install  
  
ENTRYPOINT ["react-static-serve"]  

