# Pull base image.  
FROM node:latest  
  
MAINTAINER Andrew W. <andrew.wessels@crometrics.com>  
  
# RUN apt-get update && apt-get install -y --no-install-recommends \  
# rubygems build-essential ruby-dev \  
# && rm -rf /var/lib/apt/lists/*  
  
# # Install git  
# RUN apt-get -yqq update && \  
# apt-get -yqq install git  
  
# Install Gulp & Bower  
#RUN npm install -gq gulp bower  
  
# # Global install gulp and bower  
# # --loglevel=error  
# RUN npm set progress=false && \  
# npm install --global --progress=false gulp bower npm-cache crowrap && \  
# echo '{ "allow_root": true }' > /root/.bowerrc  
  
# Install Gem Sass Compass  
# RUN gem install sass  
  
# # Binary may be called nodejs instead of node  
# RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# # Cleanup image  
# RUN apt-get -yqq autoremove && \  
# apt-get -yqq clean && \  
# rm -rf /var/lib/apt/lists/* /var/cache/* /tmp/* /var/tmp/*  
  
# RUN usermod -u ${DOCKER_USER_ID:-1000} www-data \  
# && mkdir -p ${APP_BASE_DIR:-/var/www/}  
  
# WORKDIR ${APP_BASE_DIR:-/var/www/}  
  
RUN npm set progress=false && \  
npm install --global --progress=false crowrap  
  
# ENTRYPOINT ["/bin/bash"]  
ENTRYPOINT ["node", "/usr/local/lib/node_modules/crowrap/bin/crowrap.js"]  
# CMD ["/usr/bin/crowrap"]  

