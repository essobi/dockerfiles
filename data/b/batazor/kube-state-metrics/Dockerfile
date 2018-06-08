FROM golang:1.8-alpine  
  
ENV KUBE_STATE_VERSION v0.4.1  
# Build kube-state-metrics  
WORKDIR /src  
RUN \  
apk --no-cache add git make && \  
cd /go/src && \  
git clone \--depth 1 --branch ${KUBE_STATE_VERSION}
https://github.com/kubernetes/kube-state-metrics.git && \  
cd /go/src/kube-state-metrics && \  
make build && \  
mv kube-state-metrics /src && \  
rm -rf /go/src/kube-state-metrics  
  
EXPOSE 8080  
ENTRYPOINT ["/src/kube-state-metrics", "--port=8080"]  

