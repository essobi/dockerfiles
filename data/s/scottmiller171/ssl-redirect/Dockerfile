FROM golang:1.9 as test  
WORKDIR /go/src/app  
COPY main.go .  
RUN go get -d -v ./...  
RUN go run main.go & \  
sleep 4 && \  
curl -s localhost:80/test && \  
curl -s localhost:80/test | grep '<a href="https://localhost/test">Moved
Permanently</a>.'  
  
FROM golang:1.9 as builder  
COPY main.go .  
RUN CGO_ENABLED=0 go build -a -ldflags '-s' -o /go-redirect .  
  
###############################################################################  
FROM scratch  
LABEL maintainer="Scott Miller <scott.miller171@gmail.com>"  
  
COPY --from=builder /go-redirect /go-redirect  
EXPOSE 80  
ENTRYPOINT [ "/go-redirect" ]  

