FROM golang:1.8  
ENV SRC_DIR $GOPATH/src/github.com/MSC-XDU/playground  
  
ENV PLAYGROUND_TEMP_DIR /tmp  
VOLUME /tmp  
  
COPY . $SRC_DIR  
  
WORKDIR $SRC_DIR  
  
RUN go install  
  
COPY assets/ $GOPATH/bin/assets/  
  
EXPOSE 80  
ENTRYPOINT playground

