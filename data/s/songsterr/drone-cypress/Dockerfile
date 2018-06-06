FROM cypress/base:10  
RUN mkdir -p /test  
WORKDIR /test  
  
COPY package.json yarn.lock /test/  
RUN yarn install --production --frozen-lockfile --non-interactive  
COPY json-reporter.js slack-notify.js reporter.json /test/  
  
ADD script.sh /bin/  
RUN chmod +x /bin/script.sh  
ENTRYPOINT /bin/script.sh  

