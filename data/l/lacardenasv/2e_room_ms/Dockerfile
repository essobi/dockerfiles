FROM golang:1.9  
# Setting up working directory  
WORKDIR /go/src/gin-container  
ADD . /go/src/gin-container  
  
RUN go get github.com/gin-gonic/gin  
RUN go get github.com/jinzhu/gorm  
RUN go get github.com/jinzhu/gorm/dialects/mysql  
  
# Restore godep dependencies  
#RUN godep restore  
EXPOSE 4001  
ENTRYPOINT ["/usr/local/go/bin/go"]  
CMD ["run", "src/main.go"]  
  
#https://github.com/EarvinKayonga/gin-container/blob/master/Dockerfile

