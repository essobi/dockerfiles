FROM golang:latest AS build  
  
ENV PROJECT /go/src/github.com/zcong1993/telnetor  
  
RUN mkdir -p $PROJECT  
COPY . $PROJECT  
  
WORKDIR ${PROJECT}  
  
RUN make install \  
&& CGO_ENABLED=0 make build  
  
FROM alpine:3.7  
ENV PROJECT /go/src/github.com/zcong1993/telnetor  
  
WORKDIR /opt/telnetor  
  
RUN apk add --no-cache ca-certificates  
  
COPY \--from=build $PROJECT/bin/* /usr/local/bin/  
  
RUN ln -s /usr/local/bin/telnetor* / \  
&& ln -s /usr/local/bin/telnetor* /bin/  
  
EXPOSE 10101  
CMD ["telnetor-server"]  

