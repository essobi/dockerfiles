FROM golang:1.10 as builder  
WORKDIR /go/src/github.com/awprice/agones-factorio  
RUN go get github.com/golang/dep/cmd/dep  
ADD Gopkg.toml Gopkg.lock ./  
ADD Makefile ./  
RUN make setup  
  
ADD cmd/ cmd/  
RUN CGO_ENABLED=0 go build -a -installsuffix cgo -o agones-factorio-sdk
cmd/main.go && chmod +x agones-factorio-sdk  
  
FROM dtandersen/factorio:stable  
COPY \--from=builder /go/src/github.com/awprice/agones-factorio/agones-
factorio-sdk /bin/agones-factorio-sdk  
ADD run.sh /run.sh  
ENTRYPOINT ["/run.sh"]

