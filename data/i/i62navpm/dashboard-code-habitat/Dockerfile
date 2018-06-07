FROM node:alpine  
  
ARG app_env  
ENV APP_ENV $app_env  
  
RUN mkdir -p /usr/src/app  
COPY . /usr/src/app  
WORKDIR /usr/src/app  
  
RUN yarn  
  
CMD yarn global add http-server && \  
yarn test && \  
yarn build && \  
hs dist/ -p 4000;  
  
EXPOSE 4000  

