# Dockerfile  
  
FROM alpine:3.3  
MAINTAINER @pottava  
  
LABEL com.github.pottava.application="slack-invite" \  
com.github.pottava.usage="docker run -d -p 80:80 -e SLACK_TEAM_NAME -e
SLACK_TEAM_DOMAIN -e SLACK_TOKEN pottava/slack-invite" \  
com.github.pottava.license="MIT"  
  
ENV GOPATH=/go PATH=/go/bin:$PATH LANGUAGE=en  
  
RUN apk --no-cache add \--virtual build-dependencies go git \  
&& mkdir -p /go/src /go/bin \  
&& chmod -R 777 /go \  
&& go get -u github.com/pottava/slack-invite \  
&& apk del --purge build-dependencies \  
&& rm -rf /go/pkg /go/src  
  
EXPOSE 80  
  
ENTRYPOINT ["/go/bin/slack-invite"]  

