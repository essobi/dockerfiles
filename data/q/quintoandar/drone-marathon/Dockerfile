FROM golang:1.9-alpine  
WORKDIR /go/src/github.com/quintoandar/drone-marathon  
ADD . .  
RUN GOOS=linux CGO_ENABLED=0 go build -o /bin/drone-marathon \  
github.com/quintoandar/drone-marathon  
  
FROM scratch  
COPY \--from=0 /bin/drone-marathon /bin/drone-marathon  
ENTRYPOINT ["/bin/drone-marathon"]  

