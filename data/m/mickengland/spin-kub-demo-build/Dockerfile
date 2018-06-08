FROM golang  
  
ADD . /go/src/github.com/mickengland/spin-kub-demo  
  
RUN go install github.com/mickengland/spin-kub-demo  
  
ADD ./content /content  
  
ENTRYPOINT /go/bin/spin-kub-demo  

