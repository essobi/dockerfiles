FROM node:6.2  
WORKDIR /var/www/frontend  
  
RUN echo "export TERM=xterm" >> ~/.bashrc  
  
COPY ./ /var/www/frontend  
  
EXPOSE 3000  
RUN npm install;  
  
RUN npm run typings install;  
  
CMD npm start;

