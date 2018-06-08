FROM ontouchstart/alpine-go  
RUN apk add --update git  
RUN go version  
ENV GOPATH /gobook  
ENV CGO_ENABLED 0  
RUN go get -d gopl.io/ch1/helloworld  
RUN go run gobook/src/gopl.io/ch1/helloworld/main.go  
ENTRYPOINT ["sh"]  

