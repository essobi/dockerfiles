FROM golang  
  
MAINTAINER Tsuzu  
  
VOLUME /mail  
  
RUN mkdir $GOPATH/src/sendmail  
COPY ./main.go $GOPATH/src/sendmail  
RUN go get sendmail  
RUN cp $GOPATH/bin/sendmail /mail  
  
ENTRYPOINT cp $GOPATH/bin/sendmail /mail

