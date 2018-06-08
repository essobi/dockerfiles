FROM node:8.9.1-alpine  
WORKDIR /user/src/app  
ENV NODE_ENV=production  
  
RUN npm install -g -s --no-progress yarn create-react-app  
  
# Client  
ADD client/package.json client/yarn.lock /client-dependencies/  
RUN cd /client-dependencies && yarn  
ADD client /client  
RUN rm -rf /client/node_modules && ln -s /client-dependencies/node_modules
/client  
RUN cd /client && yarn build && cp -r /client/build /user/src/app/public  
RUN rm -rf /client && rm -rf /client-dependencies  
  
# Install node_modules with yarn server  
ADD package.json yarn.lock /dependencies/  
RUN cd /dependencies && yarn  
# Copy app  
COPY . /user/src/app  
RUN rm -rf /user/src/app/node_modules && ln -s /dependencies/node_modules
/user/src/app  
  
  
EXPOSE 3045  
CMD [ "npm", "start" ]

