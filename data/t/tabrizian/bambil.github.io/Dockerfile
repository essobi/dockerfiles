FROM banian/node  
  
ENV HOST=0.0.0.0  
CMD npm start  
EXPOSE 3000  
COPY package.json yarn.lock /usr/src/app/  
RUN yarn  
  
COPY . /usr/src/app  
RUN yarn build  
  

