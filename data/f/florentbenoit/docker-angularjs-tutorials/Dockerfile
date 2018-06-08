FROM codenvy/angular-yeoman  
  
ADD package.json /tmp/application/package.json  
ADD bower.json /tmp/application/bower.json  
  
RUN cd /tmp/application && \  
npm install && \  
cp -a /tmp/application/node_modules /home/user/application/  
  
RUN cd /tmp/application && \  
bower install && \  
mkdir /home/user/application/app && \  
cp -a /tmp/application/bower_components /home/user/application/app/  
  
# 1. Use ADD instruction as root.  
ADD . /tmp/app/  
RUN cd /tmp/app && \  
cp -a /tmp/app/. /home/user/application/  
  

