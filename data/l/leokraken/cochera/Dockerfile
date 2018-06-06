FROM node:0.10.38  
MAINTAINER Bixlabs, bixlabs@bixlabs.com  
  
WORKDIR /home/mean  
  
# Install Mean.JS Prerequisites  
RUN npm install -g grunt-cli bower  
  
ADD package.json /home/mean/package.json  
RUN npm install  
  
# Manually trigger bower. Why doesnt this work via npm install?  
#ADD .bowerrc /home/mean/.bowerrc  
ADD bower.json /home/mean/bower.json  
RUN bower install --config.interactive=false \--allow-root  
  
# Make everything available for start  
ADD . /home/mean  
  
ENV NODE_ENV development  
  
EXPOSE 8080 35729  
CMD ["grunt"]  

