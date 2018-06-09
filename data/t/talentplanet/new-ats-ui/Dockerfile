FROM mhart/alpine-node:6  
ENV API_URL http://35.167.157.154:3000  
RUN apk --update add git ncdu python make g++  
  
RUN npm install -g yarn serve  
  
WORKDIR /app  
  
ADD . /app  
  
RUN yarn install  
  
RUN npm run build  
  
EXPOSE 8888  
ENTRYPOINT ["npm", "run", "serve-build"]  

