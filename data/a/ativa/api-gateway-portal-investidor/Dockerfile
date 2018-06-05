FROM node:8.9.3  
# comentar a linha acima e descomentar a linha abaixo se API precisar de
conexão com o Oracle  
# FROM ativa/node-oracle-instant-client  
WORKDIR /app  
  
COPY . .  
  
RUN apt-get update && \  
apt-get -y install sudo  
  
# RUN rm -rf node_modules && npm cache clean --force  
RUN sudo npm install --production --unsafe-perm=true \--allow-root  
  
# retirar comentário da linha abaixo se sua API precisar de conexão com o
Oracle  
# RUN chmod -x /app/node_modules/oracledb/build/Release/oracledb.node && chmod
744 /app/node_modules/oracledb/build/Release/oracledb.node  
CMD \  
npm start  
  
EXPOSE 3000  

