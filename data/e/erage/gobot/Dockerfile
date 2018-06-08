FROM golang:latest  
RUN mkdir /app  
ADD . /app/  
WORKDIR /app  
RUN go get gopkg.in/tucnak/telebot.v2  
RUN go build -o main .  
CMD ["/app/main"]

