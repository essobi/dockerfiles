FROM golang:1.10.0 as builder  
WORKDIR /go/src/github.com/zewa-crit/zewa-bot/  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
COPY main.go .  
ADD commands ./commands  
ADD util ./util  
RUN go get -d -v github.com/bwmarrin/discordgo \  
&& go get -d -v github.com/peuserik/go-warcraftlogs \  
&& go get -d -v github.com/FuzzyStatic/blizzard \  
&& go get -d -v github.com/knspriggs/go-twitch \  
&& CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o bot .  
  
  
FROM alpine:latest  
RUN apk --no-cache add ca-certificates  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
LABEL "maintainer"="zewa-crit" \  
"org.label-schema.base-image.name"="alpine" \  
"org.label-schema.base-image.version"="latest" \  
"org.label-schema.description"="zewa discord bot" \  
"org.label-schema.vcs-url"="https://github.com/zewa-crit/zewa-bot" \  
"org.label-schema.schema-version"="1.0.0-rc.1" \  
"org.label-schema.vcs-ref"=$VCS_REF \  
"org.label-schema.version"=$VERSION \  
"org.label-schema.build-date"=$BUILD_DATE  
WORKDIR /root/  
COPY \--from=builder /go/src/github.com/zewa-crit/zewa-bot/bot .  
CMD ["./bot"]  

