FROM node:7.8  
MAINTAINER Rogier Slag  
  
# Make the machine up to date and install some dependencies  
RUN apt-get update && \  
apt-get install -y git curl && \  
apt-get autoremove -y && \  
apt-get clean  
  
RUN mkdir /opt/entry  
RUN mkdir /opt/entry/server  
RUN mkdir /opt/entry/web  
EXPOSE 8080  
# Add the dependencies  
ADD package.json /opt/entry/  
ADD server/package.json /opt/entry/server/  
ADD web/package.json /opt/entry/web/  
ADD server/yarn.lock /opt/entry/server/  
ADD web/yarn.lock /opt/entry/web/  
  
RUN cd /opt/entry && npm run syncinstall  
  
# Add the app  
ADD server/helpers /opt/entry/server/helpers  
ADD server/routes /opt/entry/server/routes  
ADD server/config.js /opt/entry/server/  
ADD server/index.js /opt/entry/server/  
  
ADD web/public /opt/entry/web/public  
ADD web/src /opt/entry/web/src  
  
RUN cd /opt/entry && npm run build  
  
# Run the entire thing!  
WORKDIR /opt/entry  
CMD ["npm", "start"]  

