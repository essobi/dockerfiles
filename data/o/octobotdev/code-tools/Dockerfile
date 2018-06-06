FROM node:latest  
LABEL maintainer "jsaavedra@octobot.io"  
  
VOLUME /var/code/  
WORKDIR /var/code/  
  
RUN apt-get update &&\  
apt-get -y install python3 python3-pip &&\  
pip3 install flake8 &&\  
npm install -g eslint-config-airbnb-base eslint eslint-config-defaults \  
eslint-config-airbnb eslint-config-eslint eslint-plugin-angular \  
eslint-plugin-react eslint-plugin-react-native eslint-plugin-import \  
eslint-plugin-jsx-a11y babel-eslint  

