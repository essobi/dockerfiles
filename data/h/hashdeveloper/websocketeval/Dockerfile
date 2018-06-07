FROM ubuntu:14.04  
MAINTAINER Holger Harms "kontakt@hash-developer.de"  
# Install necessary software  
RUN apt-get update && apt-get install -y \  
nodejs-legacy \  
php5 \  
npm \  
vim  
  
# Bundle app source  
# COPY ./src /websocketeval/  
# Create symbolic link 'node' to find 'nodejs' exec - commented out because of
usage of nodejs-legacy above  
# RUN ln -s /usr/bin/nodejs /usr/bin/node  
# Tells the container to which port to listen to  
EXPOSE 8080  
# Start server and script  
ENTRYPOINT ["/usr/bin/node", "/root/prototype-one/server.js"]  
CMD ["/usr/bin/php", "/root/prototype-one/changeFile.php"]  

