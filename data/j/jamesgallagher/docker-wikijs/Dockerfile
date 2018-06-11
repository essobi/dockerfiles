FROM node:6.10.0-alpine  
  
# Need git for the npm installations below  
RUN apk update && apk add --no-cache git  
  
RUN mkdir /var/www  
WORKDIR /var/www  
RUN touch .first-run  
RUN npm install wiki.js@latest  
RUN npm install  
# pm2 will be used to run the configured Wiki.js  
RUN npm install -g pm2  
  
# Can't think of an alternative way of offering first run configuration and
then normal running other than  
# using this shell script to alternate between running 'node wiki configure'
and 'node wiki start' but  
# with the pm2 process not being sent to the background via a pm2.disconnect()  
RUN cp server/init.js server/init.js.orig  
# Comment out the pm2.disconnect() - this probably does something terrible I
don't have enough knowledge to understand ...  
RUN sed '/startInBackgroundMode/,/catch/
s/pm2.disconnect()/\/\/pm2.disconnect/' < server/init.js >
server/docker.init.js && mv server/docker.init.js server/init.js  
  
RUN echo -e "#!/bin/sh\nif [ -f /var/www/.first-run ]\nthen\n node wiki
configure; rm /var/www/.first-run \nelse\n cd /var/www && node wiki
start\nfi\n" > /var/www/start.sh  
RUN chmod +x /var/www/start.sh  
  
CMD ["/var/www/start.sh"]  
  
EXPOSE 3000  
EXPOSE 80  

