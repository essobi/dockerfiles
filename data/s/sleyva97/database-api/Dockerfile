FROM golang:1  
WORKDIR /go/src/github.com/srleyva/database-api  
ADD . ./  
RUN go get ./...  
RUN CGO_ENABLED=0 GOOS=linux go build -a -ldflags '-extldflags "-static"'
main.go  
  
# Inject binary into container  
FROM scratch  
COPY \--from=0 /go/src/github.com/srleyva/database-api/main /bin/main  
ENTRYPOINT [ "/bin/main" ]  

