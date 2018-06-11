FROM node:8  
RUN mkdir /code  
ADD . /code  
WORKDIR /code  
  
RUN yarn install  
  
EXPOSE 3000  
CMD ["npm", "start"]

