FROM alpine:latest  
  
RUN apk add --update --no-cache curl socat  
ADD ./slack-notifier.sh /usr/local/bin  
  
ENTRYPOINT ["/usr/local/bin/slack-notifier.sh"]  

