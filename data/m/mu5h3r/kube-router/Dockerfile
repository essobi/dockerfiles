FROM amd64/golang:1.10-alpine AS builder  
  
ENV GOARCH=amd64  
  
RUN apk add --no-cache \  
git  
  
COPY ./app /go/src/github.com/cloudnativelabs/kube-router/app  
COPY ./vendor /go/src/github.com/cloudnativelabs/kube-router/vendor  
COPY ./utils /go/src/github.com/cloudnativelabs/kube-router/utils  
COPY ./kube-router.go /go/src/github.com/cloudnativelabs/kube-router/  
WORKDIR /go/src/github.com/cloudnativelabs/kube-router  
  
RUN CGO_ENABLED=0 go get github.com/osrg/gobgp/gobgp  
RUN CGO_ENABLED=0 go build -o kube-router kube-router.go  
  
FROM amd64/golang:1.10-alpine  
  
RUN apk add --no-cache \  
iptables \  
ipset \  
iproute2 \  
ipvsadm \  
conntrack-tools \  
curl \  
bash && \  
mkdir -p /var/lib/gobgp && \  
mkdir -p /usr/local/share/bash-completion && \  
curl -L -o /usr/local/share/bash-completion/bash-completion \  
https://raw.githubusercontent.com/scop/bash-completion/master/bash_completion  
  
ADD build/image-assets/bashrc /root/.bashrc  
ADD build/image-assets/profile /root/.profile  
ADD build/image-assets/vimrc /root/.vimrc  
ADD build/image-assets/motd-kube-router.sh /etc/motd-kube-router.sh  
  
COPY \--from=0 /go/src/github.com/cloudnativelabs/kube-router/kube-router
/usr/local/bin/  
COPY \--from=0 /go/bin/gobgp /usr/local/bin/  
  
RUN cd && \  
/usr/local/bin/gobgp --gen-cmpl --bash-cmpl-file /var/lib/gobgp/gobgp-
completion.bash  
  
WORKDIR "/root"  
ENTRYPOINT ["/usr/local/bin/kube-router"]  

