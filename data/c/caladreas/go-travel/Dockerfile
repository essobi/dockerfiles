FROM golang:1.10 AS build  
WORKDIR /src  
ENV LAST_UPDATE=20180209  
RUN go get -v github.com/gorilla/mux/...  
RUN go get -v gopkg.in/mgo.v2/bson  
RUN go get -v gopkg.in/mgo.v2  
ADD . /src  
RUN go test \--cover ./...  
RUN go build -v -tags netgo -o go-travel  
  
FROM alpine:3.7  
ENV LAST_UPDATE=20180506  
ENV DB db  
LABEL authors="Joost van der Griendt <joostvdg@gmail.com>"  
LABEL version="0.1.0"  
LABEL description="Docker image for Go! Travel!"  
EXPOSE 8888  
CMD ["go-travel"]  
HEALTHCHECK \--interval=5s --start-period=3s --timeout=5s CMD wget -qO-
"http://localhost:8888/trips"  
COPY \--from=build /src/go-travel /usr/local/bin/go-travel  
RUN chmod +x /usr/local/bin/go-travel  

