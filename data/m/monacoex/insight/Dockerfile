FROM node:6.9.4  
# for force automated-build  
RUN echo 4  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y libzmq3-dev  
RUN npm install --unsafe-perm -g monacore-node@3.1.3-pre-7  
USER node  
WORKDIR /home/node  
RUN monacore-node create insight --testnet  
WORKDIR /home/node/insight  
RUN monacore-node install insight-api-monacoin  
RUN monacore-node install insight-ui-monacoin  
  
VOLUME /home/node/insight/data  
CMD /home/node/insight/node_modules/monacore-node/bin/monacore-node start  
  
EXPOSE 3001 9401  

