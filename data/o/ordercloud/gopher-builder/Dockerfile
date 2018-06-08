FROM node:0.12  
# Install bower & gulp globally  
RUN npm install -g bower gulp  
  
# Make work directory  
RUN mkdir -p /data  
RUN mkdir -p /data/www  
  
# Add npm + bower files  
ADD package.json /data/  
ADD bower.json /data/  
ADD .bowerrc /data/  
  
WORKDIR /data  
  
RUN npm install  
RUN bower install --allow-root  
  
RUN addgroup --gid 5011 jenkins  
RUN useradd jenkins -u 5008 -g 5011  
RUN chown -R jenkins:jenkins /data/www  

