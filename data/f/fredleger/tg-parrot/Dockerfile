FROM golang:1.8.3-alpine3.6  
ENV TG_TOKEN ""  
RUN apk add --no-cache git  
  
WORKDIR /go/src/github.com/fredleger/CocoTelegramParrotBot/cocobot  
COPY src /go/src  
  
RUN go-wrapper download && \  
go-wrapper install  
  
CMD ["go-wrapper", "run"]  

