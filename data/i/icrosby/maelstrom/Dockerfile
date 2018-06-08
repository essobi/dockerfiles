FROM golang  
  
ADD . /go/src/github.com/idcrosby/maelstrom  
WORKDIR /go/src/github.com/idcrosby/maelstrom  
  
RUN go get google.golang.org/cloud/compute/metadata  
RUN go get gopkg.in/mgo.v2  
  
RUN go install github.com/idcrosby/maelstrom  
  
ENTRYPOINT /go/bin/maelstrom  
  
EXPOSE 8123

