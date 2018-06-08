FROM node:alpine  
  
COPY user-settings.json /root/.local/share/.nativescript-cli/user-
settings.json  
  
RUN npm install -g nativescript \  
&& tns setup cloud  

