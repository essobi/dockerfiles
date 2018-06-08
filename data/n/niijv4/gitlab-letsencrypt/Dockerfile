FROM node:9.4-alpine  
  
ENV PATH="/home/node/.npm-global/bin:${PATH}"  
ENV NPM_CONFIG_PREFIX=/home/node/.npm-global  
  
RUN apk add \--no-cache --virtual build-dependencies \  
build-base \  
python \  
git \  
&& su node -c "npm install --quiet --production --no-progress -g
https://github.com/niijv/gitlab-letsencrypt.git" \  
&& apk del build-dependencies  
  
USER node  
  
ENTRYPOINT ["gitlab-le"]

