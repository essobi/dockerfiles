FROM yobasystems/alpine-golang:amd64  
LABEL maintainer "Dominic Taylor <dominic@yobasystems.co.uk>"
architecture="AMD64/x86_64"  
  
RUN apk --update add curl git && \  
curl -s -L https://github.com/rodcorsi/mattermail/releases | \  
egrep -o
'/rodcorsi/mattermail/releases/download/[0-9.]*/mattermail-.*linux.am64.tar.gz'
| head -1 | \  
(curl -Lo /tmp/mattermail.tgz http://github.com/`cat`) && \  
tar xvfz /tmp/mattermail.tgz -C /tmp && \  
rm -f /tmp/mattermail.tgz && rm -rf /var/cache/apk/  
  
RUN go get github.com/rodcorsi/mattermail | true  
  
CMD /go/bin/mattermail -c /config.json  

