FROM alpine:3.4  
MAINTAINER "European Environment Agency (EEA): IDM2 A-Team" <eea-edw-a-team-
alerts@googlegroups.com>  
  
RUN apk add --update python3 \  
&& pip3 install chaperone \  
&& apk --no-cache add curl  
  
RUN mkdir -p /etc/chaperone.d  
COPY chaperone.conf /etc/chaperone.d/chaperone.conf  
  
ENTRYPOINT ["/usr/bin/chaperone"]  

