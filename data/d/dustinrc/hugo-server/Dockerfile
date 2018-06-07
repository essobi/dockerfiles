FROM alpine:3.2  
MAINTAINER Dustin Chapman <dustin.r.chapman@gmail.com>  
  
ENV REFRESHED_AT="20150710"  
RUN apk update && apk upgrade && apk add \  
curl \  
git \  
&& rm -rf /var/cache/apk/*  
  
ENV HUGO_VERSION="0.14"  
RUN mkdir /hugo && \  
cd /hugo && \  
curl -L
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/hugo_${HUGO_VERSION}_linux_amd64.tar.gz
\  
| tar zxf - && \  
find /hugo -type f -perm /u+x -name "hugo*" -exec mv {} /usr/bin/hugo \; && \  
cd / && \  
rm -rf /hugo  
  
WORKDIR /src  
ENV GIT_POLL_INTERVAL="1h"  
ENV GIT_REMOTE_NAME="origin"  
ENV GIT_BRANCH="master"  
ADD ./poll_and_serve.sh /usr/bin/  
  
EXPOSE 1313  
ENTRYPOINT ["poll_and_serve.sh"]  
CMD [""]  

