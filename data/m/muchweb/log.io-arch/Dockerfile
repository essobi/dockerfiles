FROM base/archlinux:latest  
  
# Updating pacman repository index  
RUN pacman -Syy  
  
# Installing "node.js" and "node-gyp" build dependencies  
RUN pacman --noconfirm -S nodejs python2 make gcc  
  
# Installing coffeescript requirement  
RUN npm install -g coffee-script  
  
# Setting correct Python environment variable for "node-gyp"  
ENV PYTHON python2  
  
# Installing "log.io"  
RUN npm install -g --user "root" log.io  
  
# Log (server) listening port  
EXPOSE 28777  
# Web admin page port  
EXPOSE 28778  
# Running the server  
CMD ["log.io-server"]

