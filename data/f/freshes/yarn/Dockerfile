FROM node:carbon  
# Change register  
RUN echo 'sass_binary_site=https://npm.taobao.org/mirrors/node-
sass/\nphantomjs_cdnurl=https://npm.taobao.org/mirrors/phantomjs/\nelectron_mirror=https://npm.taobao.org/mirrors/electron/\nchromedriver_cdnurl=https://npm.taobao.org/mirrors/chromedriver\noperadriver_cdnurl=https://npm.taobao.org/mirrors/operadriver\nselenium_cdnurl=https://npm.taobao.org/mirrors/selenium\nnode_inspector_cdnurl=https://npm.taobao.org/mirrors/node-
inspector/' >> /root/.npmrc  
# Install yarn  
VOLUME /workspace  
WORKDIR /workspace  
RUN npm i -g yarn  
EXPOSE 8080  
CMD [ "bash" ]  

