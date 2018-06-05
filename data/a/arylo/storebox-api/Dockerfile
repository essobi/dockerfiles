FROM node:alpine  
  
WORKDIR /usr/src/app  
  
RUN apk add \--no-cache make gcc g++ python tzdata && \  
cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \  
echo "Asia/Shanghai" > /etc/timezone && \  
apk del tzdata  
  
ADD ./index.js ./tsconfig.json ./jsconfig.json ./package.json /usr/src/app/  
  
# --registry=https://registry.npm.taobao.org  
RUN npm set progress=false && npm install --no-progress  
  
ADD ./src /usr/src/app/src  
ADD ./config /usr/src/app/config  
  
RUN npm run tsc && \  
npm prune --production && \  
npm install cross-env tsconfig-paths typescript tslib --save-dev && \  
npm install pm2 --global && \  
npm cache clean -f && \  
rm -rf ./package-lock.json  
  
CMD pm2 start index.js \--node-args="-r tsconfig-paths/register" -i 0 --no-
daemon  
# CMD [ "npm", "run", "start:prod" ]  
  
EXPOSE 9000  

