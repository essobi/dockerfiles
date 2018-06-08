FROM alpine:3.5  
RUN apk --no-cache add ca-certificates tini  
  
RUN apk --no-cache add \--virtual .build-deps \  
go git libc-dev \  
&& mkdir /go \  
&& GOPATH=/go go get github.com/heptio/eventrouter \  
&& cp /go/bin/eventrouter /usr/local/bin/ \  
&& mkdir /etc/eventrouter \  
&& echo '{"sink": "glog"}' > "/etc/eventrouter/config.json" \  
&& rm -rf /go \  
&& apk del .build-deps  
  
USER nobody:nobody  
  
CMD ["/sbin/tini", "--", "/usr/local/bin/eventrouter", "-v=3", "-logtostderr"]  

