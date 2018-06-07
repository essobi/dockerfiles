FROM golang:1.10  
RUN echo 'Synchronizing References in apt-get...'  
RUN apt-get update  
  
RUN echo 'Installing Unzip...'  
RUN apt-get install unzip -y  
  
RUN echo 'Grabbing AWS CLI...'  
RUN wget https://s3.amazonaws.com/aws-cli/awscli-bundle.zip  
RUN unzip awscli-bundle.zip  
  
RUN echo 'Installing AWS CLI...'  
RUN ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws  
RUN rm -rf awscli-bundle*  
  
# install tools  
RUN go get github.com/ilkka/substenv  
RUN go get -u github.com/mizoguche/migorate  
RUN go get -u github.com/golang/dep/...  
RUN go get -u github.com/goadesign/goa  
RUN go get -u github.com/goadesign/goa/goagen  
RUN cd $GOPATH/src/github.com/goadesign/goa && git checkout v1.3.1 && go
install github.com/goadesign/goa/goagen  
RUN go get -u golang.org/x/lint/golint  
  
CMD /bin/sh  

