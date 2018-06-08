FROM golang:1.8  
MAINTAINER Hayahito Kawamitsu  
  
RUN git clone https://github.com/mittz/testwebapp  
RUN cd testwebapp && go build hello.go  
  
CMD "./testwebapp/hello"

