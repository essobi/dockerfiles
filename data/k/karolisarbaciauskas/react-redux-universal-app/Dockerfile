FROM node:7.8  
MAINTAINER Acidfabric <karolis.arbaciauskas@gmail.com>  
  
RUN mkdir /app  
WORKDIR /app  
COPY package.json /app  
RUN npm install  
COPY . /app  
RUN mkdir ~/.ssh \  
&& ssh-keygen -t rsa -f ~/.ssh/id_rsa -q -P “” \  
&& chmod 700 ~/.ssh  
  
ENV NODE_ENV production  
  
EXPOSE 3000  
CMD ["npm", "run", "bs"]  

