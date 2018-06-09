FROM golang:1.7.1  
  
RUN apt-get update && apt-get install -y --no-install-recommends rsync  
RUN rm -rf /var/lib/apt/lists/*  
RUN go get github.com/govend/govend  

