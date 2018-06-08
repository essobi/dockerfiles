FROM node:latest  
  
RUN npm install -g webmention-testpinger  
  
EXPOSE "8080"  
RUN git clone https://github.com/pfefferle/node-webmention-testendpoint.git -l
/opt/webmention-testendpoint  
  
WORKDIR /opt/webmention-testendpoint  
  
RUN npm install  
  
EXPOSE "9247"  
CMD ["node", "."]  

