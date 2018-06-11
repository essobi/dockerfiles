FROM alpine:3.4  
ADD . /  
RUN apk --update add go git \  
&& ORG_PATH="github.com/Financial-Times" \  
&& REPO_PATH="${ORG_PATH}/k8s-service-watcher" \  
&& export GOPATH=/gopath \  
&& mkdir -p $GOPATH/src/${ORG_PATH} \  
&& ln -s ${PWD} $GOPATH/src/${REPO_PATH} \  
&& cd $GOPATH/src/${REPO_PATH} \  
&& go get \  
&& go test \  
&& CGO_ENABLED=0 go build -a -installsuffix cgo -ldflags "-s" -o /k8s-service-
watcher ${REPO_PATH} \  
&& apk del go git \  
&& rm -rf $GOPATH /var/cache/apk/*  
  
CMD ["/k8s-service-watcher"]  
  

