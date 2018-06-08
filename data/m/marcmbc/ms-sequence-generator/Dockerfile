FROM golang:1.6  
RUN mkdir /go/app  
ADD ./src/* /go/app/  
WORKDIR /go/app  
RUN go get -d -v  
RUN go build -o main .  
RUN chmod +x -R /go/app  
CMD ["./main"]  

