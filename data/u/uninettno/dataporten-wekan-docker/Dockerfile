FROM mquandalle/wekan:latest  
MAINTAINER Kasper Rynning-Tønnesen <kasper@kasperrt.no>  
  
WORKDIR /app  
  
#  
RUN rm -rf /built_app  
RUN curl -sL https://install.meteor.com | sed s/--progress-bar/-sL/g | /bin/sh  
RUN meteor add kasperrt:accounts-dataporten  
RUN meteor build .build --directory  
RUN cd .build/bundle/programs/server && npm install  
RUN mv /app/.build/bundle /built_app  
  
COPY lib/mongo_add.js /tmp/add/mongo_add.js  
RUN cd /tmp/add/ && npm install mongojs  
COPY lib/e.sh /entry.sh  
  
RUN rm /usr/local/bin/meteor  
  
ENTRYPOINT ["/entry.sh"]  
CMD ["node /built_app/main.js"]

