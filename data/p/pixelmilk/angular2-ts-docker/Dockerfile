# To build and run with Docker:  
#  
# $ docker build -t angular2-ts-docker .  
# $ docker run -it -v [app]:/app -e USER_ID=$(id -u) --rm -p 8080:8080
angular2-ts-docker  
#  
FROM node:latest  
  
# the port to access the BrowserSync  
EXPOSE 8080 8081  
# init user  
RUN mkdir -p /app /tmp /home/nodejs && \  
groupadd -r nodejs && \  
useradd -u 1000 -r -g nodejs -d /home/nodejs -s /sbin/nologin nodejs && \  
chown -R nodejs:nodejs /home/nodejs && \  
chown -R nodejs:nodejs /app  
  
# global dependencies  
RUN npm i --unsafe-perm=true -g grunt-cli \  
yo \  
typings \  
live-server \  
karma \  
nightwatch \  
typescript \  
generator-angular2-ts  
  
# setting up modules  
COPY payload/package.json payload/typings.json payload/run.sh /tmp/  
RUN cd /tmp && \  
npm install --unsafe-perm=true && \  
chown -R nodejs:nodejs /tmp && \  
chmod a+x /tmp/run.sh  
  
# the application folder  
WORKDIR /app  
  
# the user in the docker  
USER nodejs  
  
# command to be run on inital start  
CMD ["/tmp/run.sh"]  

