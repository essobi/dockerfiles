FROM node:7.8.0  
WORKDIR /app  
  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb http://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update -qq && \  
apt-get install -y -qq nginx yarn && \  
apt-get clean -qq  
  
COPY . ./  
RUN yarn install  
  
EXPOSE 5984  
VOLUME ["/app/data"]  
CMD ["node_modules/.bin/pouchdb-server", "--dir", "./data", "--host",
"0.0.0.0"]  

