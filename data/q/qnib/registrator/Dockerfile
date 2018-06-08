###### QNIBTerminal image  
FROM qnib/syslog  
  
# https://github.com/gliderlabs/registrator/archive/master.zip  
ENV GOPATH=/go \  
REGISTRATOR_URL=https://github.com/qnib/registrator/archive \  
REGISTRATOR_BRANCH=name_filter  
RUN dnf install -y git-core golang make bsdtar --nogpgcheck && \  
mkdir -p /go/src/github.com/gliderlabs/ && \  
curl -fsL ${REGISTRATOR_URL}/${REGISTRATOR_BRANCH}.zip | bsdtar xf - -C
/go/src/github.com/gliderlabs/ && \  
mv /go/src/github.com/gliderlabs/registrator-${REGISTRATOR_BRANCH}
/go/src/github.com/gliderlabs/registrator && \  
go get github.com/fsouza/go-dockerclient && \  
go get github.com/gliderlabs/pkg/usage && \  
go get github.com/cenkalti/backoff && \  
go get github.com/coreos/go-etcd/etcd && \  
go get github.com/hashicorp/consul/api && \  
go get github.com/qnib/registrator/bridge && \  
go get gopkg.in/coreos/go-etcd.v0/etcd && \  
cd /go/src/github.com/gliderlabs/registrator/ && \  
go build -ldflags "-X main.Version $(cat VERSION)" -o
/usr/local/bin/registrator && \  
rm -rf /go  
ADD opt/qnib/registrator/bin/start.sh /opt/qnib/registrator/bin/  
ADD etc/supervisord.d/registrator.ini /etc/supervisord.d/  
ADD etc/consul.d/registrator.json /etc/consul.d/  
ADD opt/qnib/registrator/etc/registrator_warn.json /opt/qnib/registrator/etc/  

