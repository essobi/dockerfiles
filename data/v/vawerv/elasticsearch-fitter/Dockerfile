FROM alpine:3.5  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
ENV SRC $GOPATH/src/github.com/0xBADC0FFEE/elasticsearch-filter  
  
ADD ./ $SRC  
  
WORKDIR $SRC  
  
RUN apk add --no-cache musl-dev go \  
&& go install \  
&& apk del go musl-dev \  
&& rm -rf $GOPATH/src/ \  
&& rm -rf $GOPATH/pkg/  
  
ENTRYPOINT ["elasticsearch-filter"]

