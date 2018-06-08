FROM node:latest  
  
WORKDIR /home/node  
  
COPY ./ .  
  
RUN npm install \  
&& npm install -g gulp  
  
CMD ["gulp"]  
  
EXPOSE 80  

