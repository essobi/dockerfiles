FROM google/golang  
  
WORKDIR /gopath/src/app  
RUN go get github.com/Sirupsen/logrus  
RUN go get github.com/hashicorp/consul/api  
  
ADD . /gopath/src/app/  
RUN go build -o conductor cmd/conductor/main.go && mkdir /gopath/bin && cp
conductor /gopath/bin/conductor  
  
CMD [""]  
ENTRYPOINT ["/gopath/bin/conductor"]  

