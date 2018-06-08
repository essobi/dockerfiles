FROM golang:1.7-alpine  
  
MAINTAINER Touchify <dev@touchify.co> (@touchify)  
  
RUN apk --update \--no-cache add git \  
&& go get github.com/soutenniza/nats \  
&& go get github.com/nats-io/nats-top \  
&& apk del git  
  
CMD ["sh"]  

