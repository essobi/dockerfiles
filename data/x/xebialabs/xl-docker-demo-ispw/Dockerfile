FROM golang:latest  
RUN mkdir /app  
WORKDIR /app  
COPY . .  
  
# Install the Gorilla package  
RUN go get github.com/gorilla/mux  
  
RUN go build -o main .  
CMD ["/app/main"]  

