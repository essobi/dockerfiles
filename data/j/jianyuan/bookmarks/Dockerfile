FROM alpine:3.7  
EXPOSE 80  
  
COPY . /go/src/github.com/jianyuan/bookmarks  
RUN apk --no-cache add -t build-deps libc-dev git go yarn \  
&& apk --no-cache add ca-certificates \  
&& cd /go/src/github.com/jianyuan/bookmarks/webui \  
&& yarn install \  
&& yarn build \  
&& cd /go/src/github.com/jianyuan/bookmarks \  
&& export GOPATH=/go \  
&& export PATH=$GOPATH/bin:$PATH \  
&& go get \  
&& go get github.com/rakyll/statik \  
&& go generate ./statik \  
&& go build -o /bin/bookmarks \  
&& rm -rf /go \  
&& apk del --purge build-deps  
  
ENV PORT=80  
ENTRYPOINT [ "/bin/bookmarks" ]  

