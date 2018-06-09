FROM golang  
ADD . /go/src/github.com/lujem/walkman-telegram-bot-api  
#RUN go get -v gopkg.in/telegram-bot-api.v4  
RUN go get -v github.com/nasermirzaei89/telegram-bot-api  
RUN CGO_ENABLED=0 go install -v -a -installsuffix cgo -ldflags "-w -s -X
main.buildTime=`date -u +%Y/%m/%d_%H:%M:%S`" github.com/lujem/walkman-
telegram-bot-api  
ENTRYPOINT /go/bin/walkman-telegram-bot-api  

