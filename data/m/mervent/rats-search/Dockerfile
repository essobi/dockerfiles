FROM node:latest  
  
RUN git clone https://github.com/DEgITx/rats-search.git /rats-search && \  
cd /rats-search && \  
npm install && \  
npm run buildweb  
RUN sed -i.bak '/serverDataDirectory.*/s/.\//\/rats-data/' \  
/rats-search/package.json  
  
VOLUME ["/rats-data"]  
EXPOSE 8095  
WORKDIR /rats-search  
CMD ["npm", "run", "server"]  

