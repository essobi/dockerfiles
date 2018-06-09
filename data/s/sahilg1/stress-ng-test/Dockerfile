FROM golang  
  
RUN apt-get update  
RUN apt-get install -y stress-ng  
ADD . /go/src/stress-ng  
RUN cd /go/src/stress-ng &&\  
go build &&\  
go install  
CMD stress-ng  

