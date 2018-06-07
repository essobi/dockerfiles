FROM readytalk/nodejs:latest  
RUN mkdir -p /app  
WORKDIR /app  
ADD package.json /app/  
ADD . /app  
RUN npm install  
RUN npm install request --save  
RUN npm install cheerio --save  
EXPOSE 80  
ENTRYPOINT ["/nodejs/bin/npm", "start"]

