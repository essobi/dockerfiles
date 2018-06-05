FROM nodesource/node:latest  
MAINTAINER "Vinay" <vinay@symphony.com>  
  
# Required environment variables  
ENV container docker  
  
# Create user account for bot  
RUN groupadd -g 501 butler && \  
useradd -m -u 501 -g 501 butler  
WORKDIR /home/butler  
  
# Install project root folder  
ADD . /home/butler  
  
# Add external directories (but can be overridden at docker run)  
# ADD ./bootstrap /home/butler/bootstrap  
# ADD ./env.sh /home/butler/env.sh  
# ADD ./certs /home/butler/certs/  
  
# Fixes issue https://github.com/npm/npm/issues/13306  
RUN cd $(npm root -g)/npm && npm install fs-extra && sed -i -e s/graceful-
fs/fs-extra/ -e s/fs.rename/fs.move/ ./lib/utils/rename.js  
  
# Update file permissions  
RUN chown -R butler:butler /home/butler  
# Configure bot working directory  
USER butler  
RUN npm run generate-hubot  
  
# Lets get this show on the road:  
ENTRYPOINT npm run start-bot-butler  

