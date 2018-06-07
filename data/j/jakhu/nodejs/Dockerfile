FROM jakhu/base:latest  
# Builds nodejs image  
MAINTAINER Gum-Joe "kishansambhi@hotmail.co.uk"  
# Override ENV  
ENV JAKHU_WORKER_VERSION 1.0.0  
ENV JAKHU_WORKER_NAME jakhu-docker-ubuntu-nodejs  
ENV JAKHU_OS_IMAGE ubuntu  
ENV JAKHU_OS_IMAGE_TAG latest  
ENV JAKHU_DOCKER_IMAGE nodejs  
# Install nodejs versions  
RUN source /home/jakhu/.nvm/nvm.sh && nvm install v4.0  
# Install common nodejs tools - LTS  
RUN source /home/jakhu/.nvm/nvm.sh && nvm use v4.0 && npm install -g \  
browserify \  
bower \  
express-generator \  
jake \  
grunt-cli \  
gulp-cli \  
mocha \  
istanbul \  
nodemon  
# Install common nodejs tools  
RUN source /home/jakhu/.nvm/nvm.sh && nvm use default && npm install -g \  
browserify \  
bower \  
express-generator \  
jake \  
grunt-cli \  
gulp-cli \  
mocha \  
istanbul \  
nodemon  
# Re-generate versioning  
# Pull images list  
RUN sudo chown -R jakhu /jakhuImages; cd /jakhuImages && git pull  
VOLUME /jakhuImages  
# Create version  
RUN sudo chown -R jakhu /metadata  
COPY . /jakhutools  
RUN /bin/bash -l -c "source ~/.rvm/scripts/rvm && rvm use $RUBY_VERSION &&
ruby /jakhutools/versions.rb"  
RUN chmod 700 /metadata/version.sh  
RUN chmod 777 /metadata/version.sh  
RUN sudo chmod 700 /jakhutools/info.sh  
RUN sudo chmod 777 /jakhutools/info.sh  
RUN sudo chmod 700 /runner  
RUN sudo chmod 777 /runner  
RUN sudo chmod +s /runner  
VOLUME /runner  
VOLUME /jakhutools  
CMD /jakhutools/info.sh  

