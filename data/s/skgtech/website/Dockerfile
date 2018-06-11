FROM shawnzhu/ruby-nodejs:4.2.2  
MAINTAINER skgtech <hello@skgtech.io>  
  
#RUN apt-get update  
# Install gems  
RUN gem install jekyll -v '3.1.2'  
  
# Install app npm packages  
RUN mkdir -p /app/skgtech.io/  
  
WORKDIR /app/  
  
RUN wget --no-check-certificate
https://raw.githubusercontent.com/skgtech/skgtech.github.io/master/package.json
&& \  
set progress=false && \  
npm install --progress=false  
  
# Get the github repo (no need for git)  
RUN wget --no-check-certificate
https://github.com/skgtech/skgtech.github.io/archive/master.tar.gz && \  
tar -zxvf master.tar.gz && \  
mv /app/skgtech.github.io-master/ /app/skgtech.io/ && \  
rm -rf /app/skgtech.github.io-master && \  
rm -f master.tar.gz && \  
ln -s /app/node_modules /app/skgtech.io/node_modules  
  
WORKDIR /app/skgtech.io  
VOLUME /app/skgtech.io  
  
# Expose ports to host  
EXPOSE 3000 3001  
# Default command  
CMD node_modules/.bin/gulp  

