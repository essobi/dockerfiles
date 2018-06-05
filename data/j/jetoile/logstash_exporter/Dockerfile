FROM ubuntu:17.04  
RUN apt-get update && apt-get install -y curl git  
  
ENV LOGSTASH_ENDPOINT http://localhost:9600  
ENV LOGSTASH_BIND_ADDRESS 1234  
ENV GOLANG_VERSION 1.8.3  
ENV GOLANG_DOWNLOAD_URL
https://storage.googleapis.com/golang/go$GOLANG_VERSION.linux-amd64.tar.gz  
ENV GOLANG_DOWNLOAD_SHA256
1862f4c3d3907e59b04a757cfda0ea7aa9ef39274af99a784f5be843c80c6772  
  
RUN curl -fsSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \  
&& echo "$GOLANG_DOWNLOAD_SHA256 golang.tar.gz" | sha256sum -c - \  
&& tar -C /usr/local -xzf golang.tar.gz \  
&& rm golang.tar.gz  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH  
  
ADD . $GOPATH/src/logstash-exporter  
  
RUN go get -u github.com/kardianos/govendor \  
&& go get -u github.com/DagensNyheter/logstash_exporter \  
&& cd $GOPATH/src/github.com/DagensNyheter/logstash_exporter \  
&& go build -o logstash-exporter .  
  
CMD ["/go/src/logstash-exporter/startup.sh"]  

