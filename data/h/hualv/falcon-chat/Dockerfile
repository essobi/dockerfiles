FROM golang:1.8-alpine  
  
# LABEL maintainer="laoshancun@foxmail.com"  
WORKDIR /usr/local/open-falcon  
  
EXPOSE 4567/tcp  
  
CMD ["./bin/falcon-chat"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
# copies the rest of your code  
COPY . /go/src/github.com/hualvwang/chat  
  
RUN set -ex \  
#&& echo -e
"http://mirrors.tuna.tsinghua.edu.cn/alpine/v3.4/main\\\nhttp://mirrors.tuna.tsinghua.edu.cn/alpine/v3.4/community"
> /etc/apk/repositories \  
# install dependences  
# add bash  
&& apk add \--update-cache bash supervisor \  
&& apk add --virtual .build-deps \  
# gcc \  
git \  
# make \  
# musl-dev \  
\  
&& cd /go/src/github.com/hualvwang/chat \  
&& go get -v \  
&& go build -o /usr/local/open-falcon/bin/falcon-chat main.go \  
&& mv config.tpl /usr/local/open-falcon/ \  
&& mv docker-entrypoint.sh / \  
&& chmod +x /docker-entrypoint.sh \  
&& cd /usr/local/open-falcon \  
# cleaning up  
# && rm -rf /go/src/github.com/open-falcon/falcon-plus/ \  
&& apk del .build-deps

