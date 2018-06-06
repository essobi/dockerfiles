FROM golang:1.9.2-alpine3.6  
  
RUN apk --no-cache add ca-certificates curl git make openssh-client docker
bash bc mongodb-tools \  
&& curl -s https://glide.sh/get | sh \  
&& rm -rf /tmp/glide* \  
&& sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd \  
&& mkdir -p /tmp/go/src \  
&& GOPATH=/tmp/go go get -u github.com/golang/lint/golint \  
&& mv /tmp/go/bin/golint /usr/bin/ && rm -rf /tmp/go  

