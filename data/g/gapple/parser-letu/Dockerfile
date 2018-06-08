FROM golang:latest  
RUN mkdir /app  
RUN go get gopkg.in/mgo.v2  
RUN go get gopkg.in/mgo.v2/bson  
RUN go get golang.org/x/net/html  
RUN go get github.com/blackjack/syslog  
RUN go get github.com/parnurzeal/gorequest  
RUN go get github.com/gin-gonic/gin  
ADD . /app/  
WORKDIR /app  
RUN cp -r src/goldapple /go/src  
RUN go build goldapple  
RUN go install goldapple  
RUN go build -o letu-http  
EXPOSE 8800  
CMD ["/app/letu-http"]

