FROM golang:1.9-alpine3.6  
  
RUN set -x \  
&& apk add \--no-cache \  
git \  
openssh-client \  
&& mkdir -p /root/.ssh \  
&& ssh-keyscan github.com >> /root/.ssh/known_hosts \  
&& ssh-keyscan go.googlesource.com >> /root/.ssh/known_hosts \  
&& chmod 600 /root/.ssh/* \  
&& go get -v -u github.com/client9/misspell/cmd/misspell \  
&& go get -v -u github.com/fzipp/gocyclo \  
&& go get -v -u github.com/golang/dep/cmd/dep \  
&& go get -v -u github.com/golang/lint/golint \  
&& go get -v -u github.com/gordonklaus/ineffassign \  
&& go get -v -u github.com/h12w/gosweep \  
&& go get -v -u github.com/mattn/goveralls \  
&& go get -v -u github.com/golang/dep/cmd/dep \  
&& go get -v -u golang.org/x/crypto/ssh/terminal \  
&& go get -v -u golang.org/x/net/html \  
&& go get -v -u golang.org/x/text \  
&& go get -v -u golang.org/x/tools/cmd/goimports  

