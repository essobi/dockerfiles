FROM golang:alpine  
  
RUN apk update && \  
apk add git && \  
go get -d github.com/driskell/log-courier && \  
cd /go/src/github.com/driskell/log-courier && \  
go generate . ./lc-admin && \  
go install . ./lc-admin ./lc-tlscert && \  
rm -fr /var/cache/apk/* && \  
rm -fr /usr/local/go  
  
# Configure log-courier  
ADD log-courier.conf /etc/log-courier/log-courier.conf  
CMD log-courier -config=/etc/log-courier/log-courier.conf  

