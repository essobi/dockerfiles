FROM golang  
  
ADD . /go/src/github.com/P-Krebs/gobooks  
WORKDIR /go/src/github.com/P-Krebs/gobooks  
# Build the outyet command inside the container.  
# (You may fetch or manage dependencies here,  
# either manually or with a tool like "godep".)  
RUN touch /tmp/dev.db  
RUN go get -u github.com/kardianos/govendor  
RUN govendor sync  
RUN govendor install +local  
  
ENTRYPOINT /go/bin/gobooks  
  
EXPOSE 8080

