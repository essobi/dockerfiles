FROM golang:1.5  
MAINTAINER TANABE Ken-ichi <nabeken@tknetworks.org>  
  
RUN mkdir -p /go/src/app  
WORKDIR /go/src/app  
  
RUN go-wrapper download \  
github.com/BurntSushi/toml \  
github.com/armon/consul-api \  
github.com/armon/gomdb \  
github.com/cenkalti/backoff \  
github.com/codegangsta/cli \  
github.com/crowdmob/goamz/aws \  
github.com/crowdmob/goamz/sqs \  
github.com/hashicorp/raft \  
github.com/hashicorp/raft-mdb \  
github.com/streadway/amqp \  
github.com/stretchr/testify \  
github.com/ugorji/go/codec \  
&& :  
  
COPY . /go/src/app  
  
RUN cp -f delayd.toml.docker /etc/delayd.toml && \  
useradd -m delayd && \  
install -o delayd -g delayd -m 0700 -d /var/lib/delayd  
  
RUN go-wrapper download -t ./...  
RUN go install ./...  
RUN chown delayd:delayd -R /go  
  
VOLUME ["/var/lib/delayd"]  
  
USER delayd  

