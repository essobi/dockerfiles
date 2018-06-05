FROM node:7.9.0-alpine  
  
LABEL author="astrisk"  
LABEL version="1.0.0"  
  
ENV MATTERMOST_SERVER_PORT 443  
ENV MATTERMOST_SERVER_PATH /hooks/  
ENV MATTERMOST_SERVER_PROTO https  
ENV MATTERMOST_SERVER localhost  
  
RUN apk update && apk add tzdata \  
git \  
wget  
  
WORKDIR /usr/local/  
  
RUN git clone https://github.com/vrenjith/jira-matter-bridge.git \  
&& cd jira-matter-bridge \  
&& npm install  
  
EXPOSE 3000  
WORKDIR /usr/local/jira-matter-bridge  
  
ENTRYPOINT [ "npm", "start" ]  
  

