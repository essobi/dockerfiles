# This is a build stage.  
FROM golang:1.9.0 as spoon-builder  
RUN go get -u github.com/kardianos/govendor  
ADD vendor/vendor.json /go/src/github.com/graphicweave/friendly-
spoon/vendor/vendor.json  
RUN cd /go/src/github.com/graphicweave/friendly-spoon && govendor sync  
ADD . /go/src/github.com/graphicweave/friendly-spoon  
WORKDIR /go/src/github.com/graphicweave/friendly-spoon/  
RUN CGO_ENABLED=0 go build  
  
# This is the execution stage.  
FROM golang:1.9.0-alpine3.6  
WORKDIR /root/  
RUN mkdir -p /root/photos/testTakers  
RUN mkdir -p /root/photos/images  
COPY \--from=spoon-builder /go/src/github.com/graphicweave/friendly-
spoon/friendly-spoon .  
COPY \--from=spoon-builder /go/src/github.com/graphicweave/friendly-
spoon/public ./public  
COPY \--from=spoon-builder /go/src/github.com/graphicweave/friendly-
spoon/views/tmpl ./views/tmpl  
ENV TEST_TAKER_DOCKER true  
ENTRYPOINT ["./friendly-spoon"]  
CMD ["-v"]  

