FROM golang  
  
ADD . /go/src/github.com/MISingularity/deepshare  
WORKDIR /go/src/github.com/MISingularity/deepshare  
RUN go get github.com/tools/godep  
RUN godep go build -o deepshare
/go/src/github.com/MISingularity/deepshare/cmd/deepshare/main.go  
  
#ENV _DEEPSHARE_URL_BASE_HOST http://127.0.0.1  
#ENV _DEEPSHARE_URL_BASE_PORT 8080  
#ENV REDIS_MASTER_SERVICE_HOST 127.0.0.1  
#ENV REDIS_MASTER_SERVICE_PORT 6379  
#ENV MONGO_SERVICE_HOST 127.0.0.1  
#ENV MONGO_SERVICE_PORT 27017  
CMD /go/src/github.com/MISingularity/deepshare/deepshare  
EXPOSE 8080  
EXPOSE 8000  
EXPOSE 80  

