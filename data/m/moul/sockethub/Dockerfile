FROM golang:1.6  
COPY . /go/src/github.com/moul/sockethub  
WORKDIR /go/src/github.com/moul/sockethub  
RUN make  
ENTRYPOINT ["/go/src/github.com/moul/sockethub/sockethub"]  
EXPOSE 5000  

