FROM node:8  
MAINTAINER chenjunhong@useease.com  
  
ENV server /argus-web/server  
RUN mkdir -p /argus-web/server  
## TODO: copy the code from hard disk temporary , to be change into git clone  
ADD server/ /argus-web/server  
ADD ./entrypoint.sh $server  
RUN chmod +x ${server}/entrypoint.sh \  
&& mv ${server}/entrypoint.sh /usr/local/bin/ \  
&& ln -s usr/local/bin/enytrypoint.sh /entrypoint.sh  
WORKDIR $server  
## replace the npm with cnpm for some well-known reason  
RUN npm install -g cnpm \--registry=https://registry.npm.taobao.org  
RUN cnpm install -g pm2 \  
&& cnpm install  
  
## This is not for user in china  
# RUN npm install -g pm2 \  
# && npm install  
  
EXPOSE 8080  
ENTRYPOINT ["entrypoint.sh" ]

