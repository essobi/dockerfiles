# Pull base image.  
FROM xblaster/generic_node  
  
MAINTAINER xblaster@lo2k.net  
  
RUN git clone https://github.com/xblaster/NodeTetrinet.git tetris  
WORKDIR tetris  
  
RUN npm config set registry http://registry.npmjs.org/  
  
RUN npm install  
#RUN bower install --allow-root  
WORKDIR src  
  
EXPOSE 3000  
CMD node app.js  

