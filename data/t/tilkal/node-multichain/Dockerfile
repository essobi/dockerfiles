  
FROM node:6.10.1-slim  
  
EXPOSE 9720  
ARG MC_FILE_NAME=multichain-1.0-beta-1  
COPY start_multichain_test.sh /root/  
  
RUN npm install npm@latest -g && \  
curl -o multichain.tar.gz
http://www.multichain.com/download/${MC_FILE_NAME}.tar.gz && \  
tar xzf multichain.tar.gz && \  
mv ${MC_FILE_NAME}/* /usr/local/bin/ && \  
rm -rf ${MC_FILE_NAME} && rm multichain.tar.gz  
  

