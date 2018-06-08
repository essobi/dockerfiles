FROM library/node:5.0  
MAINTAINER Tomasz Rżany <tomasz.rzany@amsterdam-standard.pl>  
  
# instal requirements  
RUN npm install -g coffee-script nunjucks && npm link nunjucks  
  
# install pushd and overwrite package json to fix hiredis outdated package  
RUN cd /opt && git clone \--branch 1.6.5 git://github.com/rs/pushd.git  
ADD package.json /opt/pushd/package.json  
RUN cd /opt/pushd && npm install  
  
# add default settings template and init script which builds final settings
file  
RUN mkdir /opt/settings  
ADD settings.coffee /opt/settings/default.coffee  
ADD init.js /opt/init.js  
  
VOLUME /opt/settings  
EXPOSE 8081  
WORKDIR /opt  
  
CMD bash -c 'node /opt/init.js && coffee /opt/pushd/pushd.coffee'

