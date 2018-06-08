FROM alpine:3.7  
MAINTAINER JG <julien@mangue.eu>  
  
COPY . /go/src/github.com/jguyomard/slackbot-links/  
  
RUN apk add --no-cache --virtual .build-deps \  
make \  
git \  
go \  
musl-dev \  
&& apk add --no-cache ca-certificates \  
&& export GOPATH=/go \  
&& cd /go/src/github.com/jguyomard/slackbot-links/ \  
&& make build \  
&& mv slackbot-links /usr/local/bin/ \  
&& rm -rf /go \  
&& apk del -f .build-deps \  
&& wget
https://gist.githubusercontent.com/jguyomard/ad4bb06aaf78d1b1a59dcd7396525e71/raw/13082106d095aca585915687b03af668a15734d4/wait-
for.sh -O /usr/local/bin/wait-for \  
&& chmod +x /usr/local/bin/wait-for  
  
VOLUME /etc/slackbot-links/  
EXPOSE 9300  
CMD slackbot-links  

