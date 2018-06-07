FROM golang:1.6.2-alpine  
  
RUN apk update && apk add curl && rm -rf /var/cache/apk/*  
  
COPY . /go/src/github.com/tombee/healthcheck  
WORKDIR /go/src/github.com/tombee/healthcheck  
RUN go build  
  
HEALTHCHECK \--interval=10s --timeout=5s --retries=5 \  
CMD curl -f http://localhost:8080/health || exit 1  
  
EXPOSE 8080  
ENTRYPOINT ["./healthcheck"]  
  

