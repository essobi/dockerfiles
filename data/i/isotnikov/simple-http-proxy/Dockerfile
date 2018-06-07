FROM node:0.10  
COPY . /src  
RUN cd /src; npm install  
ENV PROXY_HOST http://localhost:8080  
EXPOSE 8080  
CMD ["node", "/src/server.js"]  

