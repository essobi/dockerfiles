# Before using/committing this Dockerfile into your git repository,  
# make sure to replace arguments that contains [XXX] with their actual names.  
FROM node:6.2  
ENV NODE_ENV production  
  
ADD . /srv/gitlab2slack-autobot  
WORKDIR /srv/gitlab2slack-autobot  
RUN cd /srv/gitlab2slack-autobot ; npm install  
  
# All product related commands should be under npm management.  
# e.g. 'npm run build', 'npm test', 'npm start' etc.  
# Uncomment the following line if this product requires building procedures.  
# RUN npm run build;  
# Starting product  
RUN npm install -g pm2 && \  
pm2 startup  
  
CMD pm2 start --name "gitlab2slack-autobot" -i max --no-daemon gitlab2slack.js  
  
# By default all applications run on port 3000 in the container.  
# It is not recommended to change the port.  
# If you'd like the application to listen on a different port,  
# use `-p` to expose port 3000 in container to another port on host.  
EXPOSE 3000  

