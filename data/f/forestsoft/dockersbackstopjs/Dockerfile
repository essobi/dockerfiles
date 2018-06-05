FROM node:slim  
MAINTAINER Sebastian Förster "foerster@forestsoft.de"  
# environment variables  
ENV TARGET_DIR /opt/BackstopJS/  
  
# copy bower configurations  
COPY ./config/bower/.bowerrc /  
COPY ./config/npm/.npmrc /  
COPY ./start.sh /start.sh  
  
# backstopjs dependencies installation  
WORKDIR $TARGET_DIR  
  
# ubuntu packages (mainly dependencies)  
RUN apt-get -yqq update  
RUN apt-get -yqq install git-core bzip2 python libfontconfig1-dev libicu-dev
libfreetype6 libssl-dev libpng-dev libjpeg-dev  
  
# phantomjs  
RUN npm install -g phantomjs  
  
# gulp  
RUN npm install -g gulp  
  
# casperjs  
RUN npm install -g casperjs  
  
# backstopjs  
RUN npm install --save-dev --allow-root backstopjs  
  
RUN apt-get clean \  
&& rm -rf /var/lib/apt/ldists/* /tmp/* /var/tmp/*  
  
RUN echo 'alias ts="gulp test"' >> /root/.bashrc  
RUN echo 'alias ref="gulp reference"' >> /root/.bashrc  
  
WORKDIR $TARGET_DIR/node_modules/backstopjs/  
# expose port for web tool  
EXPOSE 3001  
CMD ["/bin/bash" , "/start.sh"]

