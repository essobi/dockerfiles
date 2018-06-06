FROM golang:latest  
RUN mkdir /app  
ADD . /app/  
WORKDIR /app  
RUN go get github.com/gorilla/websocket  
RUN go get github.com/lib/pq  
RUN go build src/backend/main.go  
EXPOSE 80  
ENV POSTGRES_URI
postgres://postgres:collatz@postgres:5432/collatz?sslmode=disable  
ENTRYPOINT ["/app/main"]  

