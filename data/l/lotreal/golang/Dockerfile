FROM golang:1.8.3-alpine3.6  
  
RUN apk add \--no-cache bash curl g++ gcc git glide govendor make musl-dev
openssl-dev python  
  
RUN cd /tmp && \  
git clone https://github.com/edenhill/librdkafka.git && \  
cd librdkafka && ./configure --prefix /usr && make && make install && \  
cd /go && rm -rf /tmp/librdkafka && \  
go get -u github.com/confluentinc/confluent-kafka-go/kafka  
  
RUN mkdir -p /go/src/k8s.io/kubernetes && \  
cd /go/src/k8s.io/kubernetes && \  
curl -o kubernetes-release-1.3.tar.gz -L
https://github.com/kubernetes/kubernetes/archive/v1.3.0.tar.gz && \  
tar zxvf kubernetes-release-1.3.tar.gz && \  
rm kubernetes-release-1.3.tar.gz  

