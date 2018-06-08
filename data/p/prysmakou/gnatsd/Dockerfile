FROM prysmakou/golang  
RUN git clone https://github.com/apcera/gnatsd.git
/gopath/src/github.com/apcera/gnatsd  
WORKDIR /gopath/src/github.com/apcera/gnatsd  
RUN git checkout tags/v0.5.6  
RUN go get github.com/apcera/gnatsd  
CMD /gopath/bin/gnatsd  
EXPOSE 4222  

