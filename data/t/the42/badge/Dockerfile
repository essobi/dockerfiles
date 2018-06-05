FROM golang:latest  
WORKDIR /go/src/app  
COPY . .  
  
RUN go install -v  
  
CMD ["app"]  
EXPOSE 5000  

