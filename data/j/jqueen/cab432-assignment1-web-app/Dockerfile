FROM node:latest  
  
RUN mkdir -p /application /home/nodejs && \  
groupadd -r nodejs && \  
useradd -r -g nodejs -d /home/nodejs -s /sbin/nologin nodejs && \  
chown -R nodejs:nodejs /home/nodejs  
  
WORKDIR /application  
COPY package.json typings.json /application/  
RUN npm install --unsafe-perm=true  
  
COPY . /application  
RUN chown -R nodejs:nodejs /application  
USER nodejs  
  
CMD npm start

