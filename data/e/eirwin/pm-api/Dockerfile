  
FROM golang  
  
WORKDIR /go/src/polling-machine  
ADD . /go/src/polling-machine  
  
RUN go get gopkg.in/validator.v2 && \  
go get github.com/gorilla/mux && \  
go get github.com/thoas/stats && \  
go get github.com/codegangsta/negroni && \  
go get github.com/jinzhu/gorm && \  
go get github.com/garyburd/redigo/redis && \  
go get github.com/dgrijalva/jwt-go && \  
go get github.com/rs/cors && \  
go get github.com/eirwin/polling-machine/models && \  
go get github.com/eirwin/polling-machine/users && \  
go get github.com/eirwin/polling-machine/polls && \  
go get github.com/eirwin/polling-machine/data && \  
go get github.com/pborman/uuid && \  
go install polling-machine  
  
EXPOSE 8181  
ENTRYPOINT /go/bin/polling-machine

