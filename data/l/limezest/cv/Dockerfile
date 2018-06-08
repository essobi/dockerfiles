FROM alpine:3.5  
MAINTAINER <cyril@sabourau.lt>  
  
ENV TERM xterm  
  
RUN apk update && \  
apk add --no-cache ncurses  
  
WORKDIR /app  
ADD . /app  
  
ENTRYPOINT ["/bin/sh", "cv.sh"]  

