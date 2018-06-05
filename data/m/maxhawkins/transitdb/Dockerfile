FROM golang:1.7  
COPY . /go/src/github.com/maxhawkins/transitdb  
  
RUN go get -d -v github.com/maxhawkins/transitdb/...  
RUN go install -v github.com/maxhawkins/transitdb/...  
  
CMD transitdb  

