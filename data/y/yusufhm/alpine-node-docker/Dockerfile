FROM node:8-alpine  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://bitbucket.org/yusufhm/reins" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="0.1.0"  
  
RUN npm install -g heroku-cli && \  
npm cache clear --force  
  
RUN apk add --no-cache docker openssh-client  
  
CMD [ "node" ]  

