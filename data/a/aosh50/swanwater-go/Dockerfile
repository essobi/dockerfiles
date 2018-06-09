FROM golang:1.9.0-alpine3.6 as build-env  
RUN apk update  
RUN apk add git  
  
RUN mkdir -p /go/src/farm  
WORKDIR /go/src/farm  
  
#RUN go get github.com/jasonlvhit/gocron  
RUN go get google.golang.org/appengine  
RUN go get github.com/SermoDigital/jose  
RUN go get golang.org/x/crypto/bcrypt  
RUN go get github.com/tkanos/gonfig  
RUN go get github.com/go-pg/pg  
RUN go get github.com/mattbaird/gochimp  
RUN go get github.com/gorilla/mux  
RUN go get github.com/dgrijalva/jwt-go  
RUN go get github.com/rs/cors  
RUN go get github.com/gorilla/handlers  
  
COPY ./accounts ./accounts  
COPY ./farms ./farms  
COPY ./mobs ./mobs  
COPY ./paddocks ./paddocks  
COPY ./models ./models  
COPY ./routing ./routing  
COPY ./security ./security  
COPY ./swanwater ./swanwater  
COPY ./utilities ./utilities  
COPY ./database ./database  
# COPY ./swanwater/config/appsettings.localDocker.json
./swanwater/config/appsettings.json  
COPY ./swanwater/config/appsettings.prod.json
./swanwater/config/appsettings.json  
  
WORKDIR /go/src/farm/swanwater  
RUN go build  
  
ENTRYPOINT /go/src/farm/swanwater/swanwater  
  
EXPOSE 8080  
# RUN ./swanwater  
CMD ["./swanwater"]

