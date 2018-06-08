FROM golang  
  
RUN apt install -y git  
RUN go get github.com/lib/pq  
RUN useradd -u 1000 -d /code app  
RUN chown app: -R /go /usr/local/go  
  
USER app  
WORKDIR /code  

