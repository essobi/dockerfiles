# GO & POSTGRES  
FROM golang:1.7  
RUN go get github.com/lib/pq  
  
RUN mkdir -p /app  
  
WORKDIR /app  
  
ADD . /app  
  
RUN go build ./main.go  
  
CMD ["./main"]  
  
EXPOSE 8080

