FROM alpine AS builder  
  
RUN \  
apk update && \  
apk add ca-certificates wget  
RUN wget \  
https://github.com/sensiblecodeio/hookbot/releases/download/v0.4/hookbot_linux_amd64
\  
-O /hookbot  
RUN chmod +x /hookbot  
  
FROM scratch  
COPY \--from=builder /hookbot .  
CMD ["/hookbot"]  
  

