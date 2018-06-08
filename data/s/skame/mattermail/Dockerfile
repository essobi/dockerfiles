FROM golang:1.8-alpine  
  
MAINTAINER Satoshi KAMEI "ml+github@kamei.nu"  
RUN apk --update add curl git  
RUN curl -s -L https://github.com/rodcorsi/mattermail/releases | \  
egrep -o
'/rodcorsi/mattermail/releases/download/[0-9.]*/mattermail-.*linux.am64.tar.gz'
| head -1 | \  
(curl -Lo /tmp/mattermail.tgz http://github.com/`cat`) && \  
tar xvfz /tmp/mattermail.tgz -C /tmp && \  
rm -f /tmp/mattermail.tgz && rm -rf /var/cache/apk/  
  
RUN go get github.com/rodcorsi/mattermail | true  
  
CMD /go/bin/mattermail -c /config.json  
  

