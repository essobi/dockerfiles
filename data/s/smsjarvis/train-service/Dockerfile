FROM golang  
  
RUN mkdir /app  
ADD . /app/  
  
RUN go get golang.org/x/net/html  
  
WORKDIR /app  
  
RUN go build .  
  
ENTRYPOINT /app/train-service  
  
EXPOSE 9999  

