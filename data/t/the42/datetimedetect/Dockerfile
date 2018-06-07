FROM golang:latest  
RUN apt-get update && apt-get install -y libmagic-dev  
WORKDIR /go/src/app  
COPY . .  
  
RUN go install -v  
  
CMD ["app"]  
EXPOSE 5000  

