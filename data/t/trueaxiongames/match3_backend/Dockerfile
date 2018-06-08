FROM node:8-alpine  
  
LABEL version="13" \  
description="Match3 backend" \  
maintainers="Jirarot Kateramrit <jirarot@trueaxiongames.com>; Martin Fidel
Graciano <martin@trueaxiongames.com>;"  
  
  
RUN apk add --update redis net-tools tmux mysql \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /home/node  
COPY . /home/node  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
RUN chown -R node /usr/local && chown -R node /home/node  
USER node  
EXPOSE 5000 8080  
  
RUN npm i -g pm2@2.6.0 minimatch@latest \  
&& npm i  
  
# VOLUME ["/home/node/tasks"]  
# ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["pm2-docker", "start", "-i", "0", "./node_modules/.bin/actionhero"]

