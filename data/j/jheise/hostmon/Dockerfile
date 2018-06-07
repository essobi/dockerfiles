FROM jheise/ubuntu-golang  
  
# RUN mkdir -p /go/src/hostagent  
# ADD *.go /go/src/hostagent/  
RUN go get github.com/jheise/hostmon/hostagent  
RUN go install github.com/jheise/hostmon/hostagent  
ENV ADDRESS redis  
ENV PORT 6379  
ENV INTERVAL 15  
ENV IDENTITY unnamed  
WORKDIR /srv  
CMD /go/bin/hostagent -address ${ADDRESS} -port ${PORT} -interval ${INTERVAL}
-identity ${IDENTITY}  

