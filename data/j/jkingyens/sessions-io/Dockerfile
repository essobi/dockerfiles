FROM node:4.2.1-onbuild  
RUN npm install -g grunt-cli  
VOLUME /usr/src/app/dist  
CMD grunt default && grunt gcs:prod && grunt cdn:gcs

