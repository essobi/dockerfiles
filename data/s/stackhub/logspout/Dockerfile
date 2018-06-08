FROM gliderlabs/alpine:3.1  
VOLUME /mnt/routes  
EXPOSE 8000  
ENV GOPATH /go  
RUN apk-install go git mercurial  
COPY ./logspout /go/src/github.com/gliderlabs/logspout  
WORKDIR /go/src/github.com/gliderlabs/logspout  
RUN go get && go build -ldflags "-X main.Version dev" -o /bin/logspout  
  
COPY ./kvnator /go/src/github.com/karthequian/kvnator  
WORKDIR /go/src/github.com/karthequian/kvnator  
RUN go get && go build -ldflags "-X main.Version dev" -o /bin/kvnator  
  
RUN touch /tmp/kvnator.txt  
  
ADD runner.sh /bin/runner.sh  
  
RUN chmod 744 /bin/runner.sh  
  
ENTRYPOINT ["/bin/runner.sh"]  

