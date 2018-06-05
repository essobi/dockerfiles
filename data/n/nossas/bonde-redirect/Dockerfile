FROM golang  
  
WORKDIR /go/src/github.com/bonde-redirect  
COPY . .  
  
RUN go get github.com/tools/godep  
RUN godep restore  
RUN go install github.com/bonde-redirect  
  
ENTRYPOINT /go/bin/bonde-redirect  

