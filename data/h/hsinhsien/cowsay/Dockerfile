# Cowsay Container - v0.6  
# docker run -it -v /tmp:/cow weithenn/cowsay:0.4 bash  
FROM alpine:3.6  
MAINTAINER weithenn@weithenn.org  
  
RUN apk add --no-cache perl  
  
COPY cowsay /usr/bin/cowsay  
COPY default.cow /usr/share/cowsay/default.cow  
  
CMD ["/usr/bin/cowsay","Docker is very good !"]  
  

