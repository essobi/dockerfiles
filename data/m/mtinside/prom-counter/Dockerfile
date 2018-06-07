FROM golang:1.9 as build  
WORKDIR /go/src/server  
COPY . .  
RUN go-wrapper download  
ENV CGO_ENABLED=0  
RUN go-wrapper install  
  
FROM scratch  
COPY \--from=build /go/bin/server /  
  
EXPOSE 8080  
CMD ["/server"]  

