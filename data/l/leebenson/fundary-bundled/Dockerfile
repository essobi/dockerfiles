FROM ubuntu:trusty  
  
# clean and update for a fresh install  
RUN apt-get clean && apt-get update && apt-get dist-upgrade -y  
  
# build essentials  
RUN apt-get install -y build-essential g++ git curl  
RUN apt-get install -y software-properties-common  
  
# cairo + image libs  
RUN apt-get install -y libc-dev libcairo2-dev libpng-dev libglib2.0-dev
libjpeg8-dev libjpeg-turbo8-dev libpango1.0-dev libglib2.0-dev
libfreetype6-dev libxft-dev libfontconfig1-dev libgif-dev libffi-dev  
RUN apt-get install -y graphicsmagick imagemagick  
  
# latest Node binaries  
RUN curl -sL https://deb.nodesource.com/setup_0.12 | sudo bash -  
RUN apt-get install -y nodejs  
  
# add bundled node app  
ADD bundle /app/bundle/  
  
# install npm dependencies  
WORKDIR /app/bundle  
RUN npm install fibers underscore source-map-support semver  
  
# overwrite npm-container packages with ARCH-specific versions  
WORKDIR /app/bundle/programs/server/npm/npm-container  
RUN npm install canvas@1.2.9  
RUN npm install fabric@1.5.0  
RUN npm install request@2.62.0  
RUN npm install gm@1.19.0  
RUN npm install geoip-lite@1.1.6  
RUN npm install ipware@0.0.7  
RUN npm install aws-sdk@2.2.1  
RUN npm install mandrill-api@1.0.45  
  
# pm2 for auto-restarting / auto-clustering  
RUN npm install -g pm2  
  
# re-install npms that have binary dependencies - Hack!  
RUN npm install --prefix /app/bundle/programs/server/npm/npm-bcrypt bcrypt  
  
# entry point  
ADD entrypoint.bash /app/  
RUN chmod +x /app/entrypoint.bash  
  
EXPOSE 3000  
WORKDIR /app  
ENTRYPOINT ["/app/entrypoint.bash"]  

