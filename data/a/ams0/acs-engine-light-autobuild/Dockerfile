FROM golang  
  
ENV GOPATH /gopath  
ENV PATH "${PATH}:${GOPATH}/bin"  
# change Azure to another source if you need  
RUN go get -d -v github.com/Azure/acs-engine ; exit 0 # Workaround for issues
#1068  
WORKDIR /gopath/src/github.com/Azure/acs-engine  
#RUN git checkout <branch> if you need to work with a branch  
RUN make bootstrap  
RUN make build  
  
FROM ubuntu  
COPY \--from=0 /gopath/src/github.com/Azure/acs-engine/bin/acs-engine /acs-
engine  
CMD ["/acs-engine version"]  
  

