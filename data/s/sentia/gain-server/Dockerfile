FROM node:7.4  
RUN npm i -g yarn  
  
WORKDIR /app  
  
ADD src src  
COPY package.json package.json  
  
RUN yarn  
  
RUN yarn run build  
  
ENV PORT 80  
ENV AWS_ACCESS_KEY_ID <aws_key_id>  
ENV AWS_SECRET_ACCESS_KEY=<aws_secret_access_key>  
ENV AWS_REGION=eu-west-1  
EXPOSE 80  
CMD yarn run start  

