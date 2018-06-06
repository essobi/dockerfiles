FROM node:4.2.3-wheezy  
ADD . /checklist  
WORKDIR /checklist  
RUN apt-get update && apt-get install -y ruby && gem install sass  
RUN npm install --g gulp && npm install -g bower  
RUN npm install  
RUN bower install --allow-root  
RUN gulp sass  
RUN mkdir /var/database  
EXPOSE 3000  
CMD ["npm", "start"]  
  

