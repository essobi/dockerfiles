FROM golang as build  
COPY *.go /go/src/github.com/philoserf/canary/  
WORKDIR /go/src/github.com/philoserf/canary/  
ENV CGO_ENABLED 0  
RUN go build -o /canary  
  
FROM scratch  
LABEL maintainer="mark@philoserf.com"  
COPY \--from=build canary /  
CMD ["/canary", "-h"]  

