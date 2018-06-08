FROM golang:latest  
  
RUN export GOROOT=/usr/local/go  
RUN export GOPATH=$HOME/go  
RUN export PATH=$PATH:$GOROOT/bin  
  
RUN go get github.com/garyburd/redigo/redis  
RUN go get github.com/gin-gonic/contrib/sessions  
RUN go get github.com/inconshreveable/log15  
RUN go get gopkg.in/jmcvetta/napping.v3  
RUN go get gopkg.in/mgo.v2  
RUN go get gopkg.in/mgo.v2/bson  
RUN go get -u github.com/qiniu/api.v7  
RUN go get github.com/gin-gonic/contrib/gzip  
RUN go get gopkg.in/olivere/elastic.v3  
RUN go get github.com/robfig/cron  

