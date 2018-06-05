FROM golang as BUILD  
  
WORKDIR /go/src/app  
  
COPY beansync.go .  
  
RUN go-wrapper download  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o beansync .  
  
FROM shurshun/alpine-moscow  
  
LABEL SERVICE_NAME="beansync"  
  
HEALTHCHECK CMD docker-healthcheck  
  
COPY \--from=BUILD /go/src/app/beansync /usr/local/bin/  
COPY bin/ /usr/local/bin  
  
RUN find /usr/local/bin -type f -exec chmod +x {} \;  
  
ENTRYPOINT ["beansync"]

