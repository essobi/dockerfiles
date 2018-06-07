FROM golang:rc-stretch  
  
RUN apt-get update -y -qq  
  
RUN apt-get install -y -qq --no-install-recommends graphviz  
  
RUN go get -u github.com/TrueFurby/go-callvis \  
&& cd $GOPATH/src/github.com/TrueFurby/go-callvis \  
&& make  

