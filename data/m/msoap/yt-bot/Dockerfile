# export TB_TOKEN=***  
# export YT_KEY=***  
# docker build -t yt-bot .  
# docker run -d --rm --name yt-bot --env TB_TOKEN=$TB_TOKEN --env
YT_KEY=$YT_KEY -v $PWD:/db yt-bot  
# build image  
FROM golang:alpine as go_builder  
  
RUN apk add --no-cache git  
  
ENV CGO_ENABLED=0  
RUN go get -v -a -ldflags="-w -s" github.com/msoap/etc/yt-cli  
  
# final image  
FROM msoap/shell2telegram  
  
COPY \--from=go_builder /go/bin/yt-cli /app/yt-cli  
  
CMD ["-description", "Yandex Translate bot", \  
"-cache", "3600", \  
"-shell", "", \  
"-one-thread", \  
"-persistent-users", "-users-db", "/db/yt-bot.db", \  
"/:plain_text:desc=translate text", "/app/yt-cli" \  
]  

