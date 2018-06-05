# Dockerfile  
FROM golang:1.9-alpine  
  
MAINTAINER Aksels Ledins  
  
RUN apk update && apk upgrade && \  
apk add \--no-cache bash git openssh  
  
WORKDIR /usr/src/app  
  
ADD . /usr/src/app  
  
COPY . .  
  
# dependencies  
RUN go get github.com/jinzhu/gorm  
RUN go get github.com/labstack/echo  
RUN go get github.com/satori/go.uuid  
RUN go get github.com/lib/pq  
RUN go get github.com/dgrijalva/jwt-go  
RUN go get github.com/algolia/algoliasearch-client-go/algoliasearch  
RUN go build -o core .  
  
EXPOSE 1323  
  
ENTRYPOINT [ "/usr/src/app/core" ]  

