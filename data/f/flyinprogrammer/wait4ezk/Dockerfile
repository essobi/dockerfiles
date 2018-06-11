FROM ruby:alpine  
MAINTAINER Alan Schegrer <flyinprogrammer@gmail.com>  
  
RUN apk add --update --repository http://dl-
cdn.alpinelinux.org/alpine/edge/community/ tini  
COPY wait_for_leader.rb /bin/wait_for_leader  
ENTRYPOINT ["/sbin/tini", "/bin/wait_for_leader"]  

