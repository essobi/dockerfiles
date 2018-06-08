FROM zenato/puppeteer  
ADD package.json /tmp/package.json  
RUN cd /tmp && npm install  
RUN mkdir -p /app && cp -a /tmp/node_modules /app/  
EXPOSE 3000  
WORKDIR /app  
CMD npm run start  
COPY . /app  

