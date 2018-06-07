FROM golang  
  
RUN go get github.com/tools/godep  
RUN go install github.com/tools/godep  
RUN mkdir -p cd $GOPATH/src/github.com/helderfarias/hareg  
COPY discovery $GOPATH/src/github.com/helderfarias/hareg/discovery  
COPY Godeps $GOPATH/src/github.com/helderfarias/hareg/Godeps  
COPY model $GOPATH/src/github.com/helderfarias/hareg/model  
COPY register $GOPATH/src/github.com/helderfarias/hareg/register  
COPY util $GOPATH/src/github.com/helderfarias/hareg/util  
COPY main.go $GOPATH/src/github.com/helderfarias/hareg/  
RUN cd src/github.com/helderfarias/hareg \  
&& godep restore \  
&& godep go build  
RUN cd src/github.com/helderfarias/hareg \  
&& cp hareg /usr/bin/hareg \  
&& chmod +x /usr/bin/hareg  
  
ENTRYPOINT ["/usr/bin/hareg"]  

