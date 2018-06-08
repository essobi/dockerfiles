FROM golang:1.9  
RUN \  
curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash \  
&& apt-get update \  
&& apt-get install git-lfs  
  
RUN curl -sL https://github.com/golang/dep/releases/download/v0.3.2/dep-linux-
amd64 > /go/bin/dep  
RUN chmod +x /go/bin/dep  
  
# Install go-bindata  
RUN go get -u github.com/jteeuwen/go-bindata/...  
  
RUN mkdir -p $GOPATH/src/github.com/apex  
  
RUN cd $GOPATH/src/github.com/apex \  
&& git clone -b shell_env_var_substituion https://github.com/selvakn/up  
  
RUN cd $GOPATH/src/github.com/apex/up \  
&& dep ensure  
RUN cd $GOPATH/src/github.com/apex/up \  
&& make install.deps build install  

