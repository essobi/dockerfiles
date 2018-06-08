FROM node:8  
WORKDIR /app  
COPY . /app  
  
RUN yarn  
RUN yarn build  
RUN yarn global add serve  
  
EXPOSE 3000  
CMD [ "serve", "-s", "build"]  

