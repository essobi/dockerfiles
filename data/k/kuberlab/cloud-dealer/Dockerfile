FROM kuberlab/cloud-dealer:base  
  
COPY ./pkg "$GOPATH/src/github.com/kuberlab/cloud-dealer/pkg"  
COPY ./cloud-dealer.go "$GOPATH/src/github.com/kuberlab/cloud-dealer/"  
  
RUN rm -rf $GOPATH/src/github.com/kuberlab/cloud-
dealer/vendor/github.com/kuberlab/lib \  
&& git clone https://github.com/kuberlab/lib \  
&& mv lib $GOPATH/src/github.com/kuberlab/cloud-
dealer/vendor/github.com/kuberlab/lib  
  
RUN go install "github.com/kuberlab/cloud-dealer"  
  
FROM golang:1.9.2  
RUN mkdir -p /etc/cloud-dealer/credentials \  
&& mkdir /dealer_db  
COPY ./templates "$GOPATH/templates"  
COPY ./swagger-ui "$GOPATH/swagger-ui"  
RUN date '+%Y-%m-%d %H:%M:%S' > "$GOPATH/build_time"  
  
COPY \--from=0 /go/bin/cloud-dealer /go/bin/cloud-dealer  
  
CMD [ "cloud-dealer" ]  
  
VOLUME ["/etc/cloud-dealer/credentials","/dealer_db"]  
  
EXPOSE 8082 12120 8083

