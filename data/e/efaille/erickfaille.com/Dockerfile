FROM efaille/node  
MAINTAINER Erick Faille "efaille@gmail.com"  
ADD . /data  
  
RUN npm install  
RUN npm run build  
  
EXPOSE 80  
  
CMD npm run server  

