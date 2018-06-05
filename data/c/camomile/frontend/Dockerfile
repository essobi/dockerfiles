FROM node:0.10.38  
ADD . /app  
WORKDIR /app  
RUN npm install  
RUN git clone https://github.com/pbruneau/rserve-js.git node_modules/rserve  
WORKDIR /app/node_modules/rserve  
RUN npm install  
WORKDIR /app  
  
EXPOSE 8073  
CMD ["node", "/app/web-server.js", "--pyannote=http://localhost:8071", "--
camomile=http://localhost:8070", "--analytics=http://localhost:8081", "--
login=root", "--password=password"]  

