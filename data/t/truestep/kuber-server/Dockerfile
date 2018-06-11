FROM debian:jessie as builder  
# intall gcc and supporting packages  
RUN apt-get update && apt-get install -yq make gcc  
WORKDIR /code  
# download stress-ng sources  
ARG STRESS_VER  
ENV STRESS_VER ${STRESS_VER:-0.09.10}  
ADD https://github.com/ColinIanKing/stress-ng/archive/V${STRESS_VER}.tar.gz .  
RUN tar -xf V${STRESS_VER}.tar.gz && mv stress-ng-${STRESS_VER} stress-ng  
# make static version  
WORKDIR /code/stress-ng  
RUN STATIC=1 make  
  
##- build go app  
FROM golang:latest as gobuilder  
RUN go get github.com/golang/dep/cmd/dep  
#RUN curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh  
COPY ./ $GOPATH/src/kuber-server/  
WORKDIR $GOPATH/src/kuber-server  
RUN dep ensure  
#RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o /app/kuberloader
kuberloadserver.go  
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -a -tags netgo -ldflags '-w
-extldflags "-static"' -o /app/kuberloader kuberloadserver.go  
RUN cp home.html /app/  
RUN cp -R scripts /app/  
  
## to make from scrach with certificates fro https  
FROM ubuntu:latest  
COPY \--from=builder /code/stress-ng/stress-ng /usr/local/bin  
RUN mkdir -p /app  
COPY \--from=gobuilder app/ /app/  
WORKDIR /app  
RUN ls -R  
EXPOSE 8081  
RUN chmod +x ./kuberloader  
CMD ["./kuberloader"]

