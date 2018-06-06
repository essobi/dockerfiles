#  
# hubot-weixin Dockerfile  
#  
# https://github.com/kasperdeng/hubot-wechat  
#  
# Pull base image.  
FROM mhart/alpine-node:latest  
  
MAINTAINER Kasper Deng <kasperdeng@126.com>  
  
RUN \  
apk add --no-cache git --arch x86_64 && \  
cd /root && \  
git clone https://github.com/github/hubot && \  
cd /root/hubot && \  
rm -rf /root/hubot/src && \  
echo -e '#!/bin/sh \nset -e \nexport
PATH="node_modules/.bin:node_modules/hubot/node_modules/.bin:$PATH" \nexec
node_modules/.bin/hubot "$@"' > /root/hubot/bin/hubot && \  
sed -i -e '/\"dependencies\".*/a\ \"hubot-weixin\": \"^1.0.6\",'
./package.json && \  
npm install -g coffee-script --registry=https://registry.npm.taobao.org && \  
npm install --save --registry=https://registry.npm.taobao.org  
  
# Define environment variables.  
ENV HUBOT_LOG_LEVEL debug  
  
# Define working directory.  
WORKDIR /root/hubot  
  
# Define default command.  
CMD ["bin/hubot", "-a", "weixin"]  

