FROM node:8-alpine  
LABEL Maintainer="Stefan Paletta <stefanp@nein.io>"  
RUN yarn global add --non-interactive --no-progress --no-lockfile firebase-
tools && yarn cache --non-interactive --no-progress clean  
ENTRYPOINT [ "/usr/local/bin/firebase" ]  

