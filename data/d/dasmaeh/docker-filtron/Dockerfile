# docker container running filtron, a filtering reverse proxy for webapps like
searx  
FROM golang:alpine  
MAINTAINER Jan Köster <dasmaeh@cbjck.de>  
  
# set needed variables  
ENV APP_PORT 8888  
ENV RULES_FILE /etc/filtron/example_rules.json  
  
# install git  
RUN apk add --no-cache git  
  
# install filtron  
RUN go get github.com/asciimoo/filtron  
RUN mkdir /etc/filtron  
  
EXPOSE 4004 4005  
VOLUME [ "/etc/filtron" ]  
  
ADD entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
# TODO: ENV variables will not be expanded in CMD  
# Add an entrypoint.sh to take care of this  
# This file could also copy the sample rules to /etc/filtron if not there  
# CMD ["/go/bin/filtron", "-target", "app:APP_PORT"]  

