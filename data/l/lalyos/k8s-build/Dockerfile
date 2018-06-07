FROM golang:1.9  
  
RUN go get github.com/tools/godep  
RUN go get -u k8s.io/apimachinery/...  
RUN go get k8s.io/client-go/...  
RUN go get -d k8s.io/helm 2>/dev/null || true \  
&& cd /go/src/k8s.io/helm \  
&& make bootstrap  
RUN cd $GOPATH/src/k8s.io/client-go && git checkout v3.0.0 && godep restore
./...  
RUN cd /go/src/k8s.io/helm && go install -v ./cmd/helm/  

