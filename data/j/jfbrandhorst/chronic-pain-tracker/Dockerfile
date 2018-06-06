# Build stage  
FROM golang:latest as build-env  
ADD . /go/src/github.com/johanbrandhorst/chronic-pain-tracker  
ENV CGO_ENABLED=0  
RUN cd /go/src/github.com/johanbrandhorst/chronic-pain-tracker && go build -o
/app  
  
# Production stage  
FROM scratch  
COPY \--from=build-env /app /  
  
ENTRYPOINT ["/app"]  

