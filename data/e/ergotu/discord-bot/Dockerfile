FROM golang:alpine  
  
RUN apk update &&\  
apk add git  
  
COPY discord-bot /go/discord-bot  
  
RUN go get github.com/bwmarrin/discordgo  
  
RUN cd discord-bot &&\  
go build

