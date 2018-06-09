FROM node:6.9.1  
RUN mkdir -p /usr/src/  
WORKDIR /usr/src/  
  
# Install yarn  
RUN mkdir -p /opt  
ADD latest.tar.gz /opt/  
RUN mv /opt/dist /opt/yarn  
ENV PATH "$PATH:/opt/yarn/bin"  
ADD package.json yarn.lock /usr/src/  
  
# Copy cache contents (if any) from local machine  
ADD .yarn-cache.tgz /  
  
# Install packages  
RUN cd /usr/src && yarn  
  
RUN yarn global add concurrently  
  
# Build server  
ADD . /usr/src/  
RUN yarn build-server  
  
# Apidoc  
RUN yarn add apidoc  
RUN node /usr/src/node_modules/apidoc/bin/apidoc -i /usr/src/server/ -o
/usr/src/build/apidoc/  
RUN yarn remove apidoc  
  
# App folder  
RUN mv /usr/src/build/ /usr/app  
WORKDIR /usr/app  
  
RUN yarn add babel-runtime  
RUN yarn install --production  
  
RUN rm -r /usr/src  
  
EXPOSE 80  
CMD [ "npm", "start" ]  

