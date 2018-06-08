FROM node:0.12-onbuild  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY package.json /usr/src/app/  
RUN npm install  
COPY . /usr/src/app/  
  
ENV PORT 5002  
EXPOSE 5002  
CMD ["node","bin/www"]

