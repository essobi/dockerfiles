FROM node:alpine  
LABEL maintainer="groge <groge.choi@gmail.com>"  
  
# Install pm2  
RUN npm install -g pm2 node-gyp  
RUN apk add --no-cache --update p7zip  
  
ENV NODE_ENV production  
  
EXPOSE 3000  
WORKDIR /app  
  
# Start pm2.json process file  
CMD ["pm2-runtime", "start", "pm2.json"]  
  

