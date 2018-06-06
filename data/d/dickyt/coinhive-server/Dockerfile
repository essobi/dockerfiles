FROM node:9.3-slim  
  
ENV SERVER_ROOT /coinhive-server  
ENV SSL_CERT_DIR /coinhive-server  
ENV LOG_ROOT /coinhive-server  
ENV POOL_ADDR xmr-usa.dwarfpool.com  
ENV POOL_PORT 8005  
ENV POOL_PASSWD x  
ENV POOL_USER coinhive_test  
ENV WALLET_ADDR
47o6dEd2u5rG2eGReYp6p6JZYfUsUK89u4ppYapDa41HGjV6U45CFJ7ARQS5QpqUJSiyRSjAGGWXwZ4r9FGSrXrQARt19xX  
ENV MAX_CONN 100  
# Prepare env  
RUN mkdir $SERVER_ROOT  
  
# Set working dir  
WORKDIR $SERVER_ROOT  
  
# Copy startup file  
COPY package.json ./package.json  
COPY proxy.js ./proxy.js  
COPY start.sh ./start.sh  
  
# Install packages  
RUN npm install  
  
# Expose port  
EXPOSE 8892  
# Run  
CMD bash ./start.sh  

