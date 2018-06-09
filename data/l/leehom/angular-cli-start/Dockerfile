FROM ubuntu:latest  
MAINTAINER clh021@gmail.com  
RUN apt-get update  
RUN apt-get install -y vim git nodejs npm  
RUN npm install -g typescript  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g angular-cli --no-optional  
RUN ng new workspace  
WORKDIR /workspace  
  
# Explanation  
# Here to ensure the rapid development of Chinese inland developers to use  
# Follow-up will continue to update will be perfect  
# The service needs to be turned on manually 'ng serve'  
# Thank you for your attention  
  
# 先部署好全局库，然后再设置权限和安装项目库  
# RUN chown -R $APP_USER /usr/local/lib/node_modules  
# USER $APP_USER  
# 繁琐的权限问题，忽略，直接在docker中使用root  
# RUN npm install && npm cache clean  
# RUN npm install cnpm typings  
# RUN npm run typings --install  
# RUN npm install --save @ng-bootstrap/ng-bootstrap  
# RUN npm install -g typings tsd bower gulp typings webpack-dev-server rimraf
webpack mocha http-server  
# RUN chown -R $APP_USER:$APP_USER $HOME  
# ENV HOME /home/$APP_USER  
# ENV APP_DIR $HOME/$APP_NAME  
# ENV APP_USER "app"  
# RUN useradd --user-group --create-home --shell /bin/bash $APP_USER  
# EXPOSE 4200 49152  
# CMD ["ng", "serve", "--host=0.0.0.0"]  

