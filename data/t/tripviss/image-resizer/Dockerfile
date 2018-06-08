FROM node:7  
# https://github.com/yarnpkg/yarn/issues/2266  
RUN yarn global add node-gyp  
  
WORKDIR /srv/image-resizer-instance  
  
RUN yarn global add https://github.com/tripviss/image-resizer.git#v1.7.0 \  
&& image-resizer new \  
&& yarn install --production \  
&& yarn cache clean  
  
EXPOSE 3001  
CMD ["yarn", "start"]  

