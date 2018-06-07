FROM node:wheezy  
  
MAINTAINER https://github.com/kris-davison  
  
WORKDIR /app  
  
# Install meanjs tools  
RUN npm install -g grunt-cli  
RUN npm install -g bower  
  
# Get mean quick start app  
RUN git clone https://github.com/rsdevigo/jungle.git .  
  
# ADD package.json /app  
# ADD .bowerrc /app  
# Install Mean.JS packages  
RUN npm install  
  
# Manually trigger bower. Why doesnt this work via npm install?  
RUN bower install --config.interactive=false \--allow-root  
  
# Expose ports: server (3000), livereload (35729)  
EXPOSE 3000 35729  
# default values are for development  
ENV NODE_ENV development  
ENV KONGURL http://localhost:8001  
# add startup shell script  
ADD start.sh start.sh  
  
# make sure the file is executable  
RUN chmod +x start.sh  
  
ENTRYPOINT ["./start.sh"]  

