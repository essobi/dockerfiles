FROM zenato/puppeteer  
  
USER root  
  
# It's a good idea to use dumb-init to help prevent zombie chrome processes.  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
  
# Install puppeteer so it's available in the container.  
RUN yarn add --production puppeteer mermaid.cli  
  
#USER pptruser  
ADD pconf.json /pconf.json  
  
WORKDIR /mmdc  
  
ENTRYPOINT ["dumb-init", "--", "/node_modules/.bin/mmdc", "-p", "/pconf.json"]  

