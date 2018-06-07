from quay.io/lorinma/dockeride:cpp  
MAINTAINER Ling Ma <malingreal@gmail.com>  
# WORKDIR usr/local/src/  
# installing nodejs and gyp utility to build extensions  
RUN apt-get update -y; sudo apt-get install nodejs npm -y --force-yes --fix-
missing --no-install-recommends  
RUN sudo npm install node-gyp -g  
RUN sudo npm install mocha -g  
RUN sudo ln -s /usr/bin/nodejs /usr/bin/node  
# ------------------------------------  
RUN git clone \--recursive https://github.com/erossignon/node-occ.git  
RUN cd node-occ;sudo sh prepare_build.sh;sudo npm install;sudo node-gyp
configure;sudo node-gyp build; mocha  
RUN cd node-occ/sample;sudo npm install  
  
  
# Clean up any files used by apt-get  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
WORKDIR usr/local/src/node-occ/sample  
# --node app.js  

