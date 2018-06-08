FROM golang:1.7.3  
#  
ENV MY_PROJECT /myproject  
RUN mkdir $MY_PROJECT  
  
# gopath設定  
RUN mkdir -p $MY_PROJECT/gopath  
ENV GOPATH $MY_PROJECT/gopath  
ADD ./gopath $GOPATH  
  
# goプログラム設定  
RUN mkdir -p $MY_PROJECT/golang  
RUN cp -r /usr/local/go/ $MY_PROJECT/golang/  
  
RUN mkdir -p $GOPATH/bin  
# path設定  
ENV PATH $GOPATH/bin:$MY_PROJECT/golang/go/bin:$PATH  
  
# Install a migration tool and a vendoring tool  
#RUN go run $GOPATH/src/gozen/tools/init.go  
#RUN go get bitbucket.org/liamstask/goose/cmd/goose  
#RUN go get -u github.com/kardianos/govendor  
#RUN cd $GOPATH/src/gozen && govendor sync  
# サービスとしては必要ないが、調査したいときがあるため入れておきたい  
#RUN apt-get update && apt-get install -y net-tools  
#WORKDIR $GOPATH/src/gozen  
# Unix syslog delivery error  
#
https://groups.google.com/a/codenvy.com/d/msg/codenvy/6K6SgvK09oQ/oPswTD5aCAAJ  
#RUN apt-get update -q && apt-get install -y rsyslog  
#ENTRYPOINT /usr/sbin/rsyslogd -n &  

