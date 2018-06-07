FROM emonuh/base  
MAINTAINER emonuh  
  
# install golang 1.5.1  
WORKDIR /usr/local/src  
RUN wget https://storage.googleapis.com/golang/go1.5.1.linux-amd64.tar.gz  
RUN tar -C /usr/local -xzf go1.5.1.linux-amd64.tar.gz  
  
# setting  
WORKDIR /root  
ENV PATH $PATH:/usr/local/go/bin  
RUN mkdir -p go-work/src go-work/pkg go-work/bin  
ENV GOPATH /root/go-work  
  
# clean  
RUN rm /usr/local/src/go1.5.1.linux-amd64.tar.gz  
WORKDIR $GOPATH  

