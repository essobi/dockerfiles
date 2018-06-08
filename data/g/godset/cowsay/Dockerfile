# Cowsay Container - v0.5  
# docker run -it -v /tmp:/cow godset/cowsay:0.4 bash  
FROM alpine:latest  
MAINTAINER godset@test  
RUN apk add --no-cache perl  
COPY cowsay /usr/bin/cowsay  
COPY default.cow /usr/share/cowsay/default.cow  
CMD ["/usr/bin/cowsay","Docker is very good !"]  
  

