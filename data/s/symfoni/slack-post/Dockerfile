FROM alpine:3.4  
RUN apk add --no-cache curl jq bash  
ADD slack.sh /bin/slack.sh  
RUN chmod +x /bin/slack.sh  
ENTRYPOINT ["/bin/slack.sh"]  

