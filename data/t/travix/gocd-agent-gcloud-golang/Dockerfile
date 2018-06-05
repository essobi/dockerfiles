FROM travix/gocd-agent-gcloud:18.5.0  
  
MAINTAINER Travix  
  
ENV GO_VERSION=1.8 \  
GOPATH=/var/go/gocode  
  
RUN apt-get update \  
&& apt-get install -y gcc \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& curl -fSL "https://storage.googleapis.com/golang/go${GO_VERSION}.linux-
amd64.tar.gz" -o go${GO_VERSION}.linux-amd64.tar.gz \  
&& tar -C /usr/local -xzf go${GO_VERSION}.linux-amd64.tar.gz \  
&& echo "export PATH=$PATH:/usr/local/go/bin" >> /var/go/.bashrc \  
&& rm -f go${GO_VERSION}.linux-amd64.tar.gz \  
&& /usr/local/go/bin/go get -u github.com/go-swagger/go-swagger/cmd/swagger  
  
ENV PATH /usr/local/go/bin:/var/go/gocode/bin:$PATH  

