FROM percona/percona-server-mongodb  
  
RUN curl https://storage.googleapis.com/golang/go1.6.1.linux-amd64.tar.gz |
tar -C /usr/local -xz  
RUN ln -s /usr/local/go/bin/go /usr/local/bin/go && ln -s
/usr/local/go/bin/godoc /usr/local/bin/godoc && ln -s /usr/local/go/bin/gofmt
/usr/local/bin/gofmt && mkdir $HOME/.go  
ENV GOPATH $HOME/.go  
  
RUN yum install git -y  
  
RUN go get github.com/facebookgo/rocks-strata/strata  
RUN cd $GOPATH/src/github.com/facebookgo/rocks-
strata/strata/cmd/mongo/lreplica_s3storage_driver/strata && go get ./... && go
build  
RUN ln -s $GOPATH/src/github.com/facebookgo/rocks-
strata/strata/cmd/mongo/lreplica_s3storage_driver/strata/strata
/usr/local/bin/strata  

