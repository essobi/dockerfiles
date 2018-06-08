FROM golang:1.8-alpine  
WORKDIR /go/src/github.com/quintoandar/gatekeeper  
ADD . .  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /tmp/gatekeeper
.  
  
FROM centurylink/ca-certs  
COPY \--from=0 /tmp/gatekeeper /bin/  
  
EXPOSE 8080  
ENTRYPOINT ["/bin/gatekeeper"]  

