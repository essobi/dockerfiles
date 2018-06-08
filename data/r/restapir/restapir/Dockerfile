FROM alpine:3.7  
ADD core/package.json /app/core/  
  
RUN apk update \  
&& apk add nodejs nodejs-npm make gcc g++ python \  
&& cd /app/core \  
&& npm install --production \  
&& apk del nodejs-npm make gcc g++ python \  
&& rm -Rf ~/.npm \  
&& cd /app/core/node_modules \  
&& find . -type f | grep '/test/' | xargs rm \  
&& find . -type f -iname readme.md | xargs rm \  
&& find . -type f -iname changelog.md | xargs rm \  
&& find . -type f -iname history.md | xargs rm \  
&& find . -type f -iname license | xargs rm \  
&& rm /var/cache/apk/*  
  
ADD . /app  
  
WORKDIR /app  
  
EXPOSE 80  
CMD ["node", "restapir.js"]  

