FROM node:latest  
  
RUN npm install -g --unsafe blockchain-wallet-service  
  
CMD blockchain-wallet-service start --bind 0.0.0.0 --port 3000  
  
EXPOSE 3000/tcp  

