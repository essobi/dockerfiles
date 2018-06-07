FROM node:8.9.1-alpine  
WORKDIR /app  
EXPOSE 8080  
CMD node dist/index.js  
  
ADD ./package.json yarn.lock ./  
RUN yarn --frozen-lockfile  
  
ADD ./tsconfig.build.json ./tsconfig.json ./tslint.json ./README.md ./  
ADD ./src ./src  
RUN yarn run lint && \  
yarn test && \  
yarn run build  

