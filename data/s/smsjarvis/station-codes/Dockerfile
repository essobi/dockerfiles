FROM golang  
  
RUN mkdir /app  
ADD . /app/  
  
RUN go get github.com/xrash/smetrics  
  
WORKDIR /app  
  
RUN go build .  
  
ENTRYPOINT /app/station-codes  
  
EXPOSE 8888  

