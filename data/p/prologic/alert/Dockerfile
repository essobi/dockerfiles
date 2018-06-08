FROM golang:alpine AS build  
  
RUN apk add --update git && \  
rm -rf /var/cache/apk/* && \  
go get github.com/prologic/irccat && \  
go get github.com/prologic/msgbus/...  
  
FROM alpine  
  
ENV MSGBUS_URI https://msgbus.mills.io/  
ENV MSGBUS_TOPIC alerts  
  
ENV IRC_NICK alertmanager  
ENV IRC_HOST irc.mills.io  
ENV IRC_PORT 6667  
ENV IRC_CHAN #alerts  
RUN apk add --update ca-certificates jq && \  
rm -rf /var/cache/apk/*  
  
COPY \--from=build /go/bin/irccat /usr/local/bin/irccat  
COPY \--from=build /go/bin/msgbus /usr/local/bin/msgbus  
  
COPY alert.sh /usr/local/bin/alert.sh  
COPY start.sh /start.sh  
  
ENTRYPOINT ["/start.sh"]  

