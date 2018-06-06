# docker run -d -p 2066:3200 --name scuba-master scuba-api:master  
FROM golang  
MAINTAINER William J Klos (bill.klos@centricconsulting.com)  
  
# Build the SCUBA server.  
#RUN git clone
https://wjklos:3b30f095f828c61d296e7627d70cef69de6db7dd@github.com/centricconsulting/qrcode-
api.git /go/src/github.com/centricconsulting/qrcode-api  
RUN git clone https://github.com/centricconsulting/qrcode-api.git
/go/src/github.com/centricconsulting/qrcode-api  
  
RUN go get github.com/gin-gonic/gin  
RUN go get github.com/boombuler/barcode  
RUN go get github.com/boombuler/barcode/qr  
RUN go get github.com/newrelic/go-agent  
  
RUN cd /go/src/github.com/centricconsulting/qrcode-api; go install  
  
# Start the SCUBA server.  
WORKDIR /go/src/github.com/centricconsulting/qrcode-api  
ENTRYPOINT ["qrcode-api"]  

