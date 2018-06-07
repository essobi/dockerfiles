FROM node:8-alpine  
  
COPY ./package.json ./yarn.lock /app/  
RUN cd /app && yarn install && rm -rf /root/.cache /root/.npm  
  
WORKDIR /app  
COPY . /app  
RUN yarn build  
  
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/app/bin  

