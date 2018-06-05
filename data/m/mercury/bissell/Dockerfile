FROM golang  
  
ADD bissell.go /go/src/github.com/wtsi-hgi/bissell/bissell.go  
ADD test.cram /go/test.cram  
ADD test.cram.crai /go/test.cram.crai  
  
RUN cd /go/src/github.com/wtsi-hgi/bissell && go get && go install  
  
EXPOSE 5000  
CMD bissell  

