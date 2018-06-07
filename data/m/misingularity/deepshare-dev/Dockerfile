FROM golang  
  
ADD . /go/src/deepshare  
WORKDIR /go/src/deepshare  
RUN go get -v -d  
RUN go build  
CMD /go/src/deepshare/deepshare  
#RUN go install -v deeplink/useragent deeplink  
#RUN go run deeplink  
EXPOSE 8080  

