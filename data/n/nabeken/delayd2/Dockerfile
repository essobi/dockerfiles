FROM golang:1.8  
MAINTAINER TANABE Ken-ichi <nabeken@tknetworks.org>  
  
RUN mkdir -p /go/src/github.com/nabeken/delayd2  
WORKDIR /go/src/github.com/nabeken/delayd2  
  
RUN go-wrapper download \  
github.com/aws/aws-sdk-go/... \  
github.com/cybozu-go/cmd \  
github.com/cybozu-go/log \  
github.com/cybozu-go/netutil \  
github.com/fatih/camelcase \  
github.com/google/gops/... \  
github.com/hashicorp/go-multierror \  
github.com/jessevdk/go-flags \  
github.com/kardianos/osext \  
github.com/lestrrat/go-config/env \  
github.com/lestrrat/go-pdebug \  
github.com/lib/pq \  
github.com/nabeken/aws-go-sqs/... \  
github.com/pkg/errors \  
github.com/pmylund/go-cache \  
golang.org/x/net/...  
  
COPY . /go/src/github.com/nabeken/delayd2  
  
RUN go-wrapper download ./...  
RUN go get github.com/google/gops/...  
  
RUN go install -ldflags "-X main.GitCommit=\"$(git rev-parse HEAD)\""
github.com/nabeken/delayd2  
  
RUN useradd -m delayd2 && \  
chown delayd2:delayd2 -R /go  
  
USER delayd2  

