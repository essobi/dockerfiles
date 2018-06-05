# wget  
# This seems dumb, but it lets me background wget on my docker host  
# without having to install screen/tmux  
FROM alpine:edge  
  
MAINTAINER Mark Wilkerson <mark@markwilkerson.me>  
  
RUN apk --no-cache add wget  
  
ENTRYPOINT ["/usr/bin/wget"]  
  

