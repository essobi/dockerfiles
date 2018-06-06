FROM node:8  
ARG PORT=3000  
RUN mkdir -p /app  
WORKDIR /app  
  
# only copy package.json initially so that `RUN yarn` layer is recreated only  
# if there are changes in package.json  
ADD package.json yarn.lock /app/  
  
# --pure-lockfile: Don’t generate a yarn.lock lockfile  
RUN yarn --pure-lockfile  
  
COPY . /app  
  
RUN mv .env.production .env  
  
RUN yarn build  
  
RUN cd dist  
  
CMD node dist/app.js  

