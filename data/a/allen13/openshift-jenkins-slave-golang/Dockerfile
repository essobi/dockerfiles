FROM openshift/jenkins-slave-base-centos7:latest  
  
RUN yum groupinstall 'Development Tools' -y && yum install wget -y \  
mkdir /go  
  
ENV GOLANG_VERSION 1.9  
RUN set -eux; \  
\  
url="https://golang.org/dl/go${GOLANG_VERSION}.linux-amd64.tar.gz"; \  
wget -O go.tgz "$url"; \  
echo "d70eadefce8e160638a9a6db97f7192d8463069ab33138893ad3bf31b0650a79
*go.tgz" | sha256sum -c -; \  
tar -C /usr/local -xzf go.tgz; \  
rm go.tgz; \  
export PATH="/usr/local/go/bin:$PATH"; \  
go version  
  
ENV GOROOT /usr/local/go  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:$GOROOT/bin:$PATH  

