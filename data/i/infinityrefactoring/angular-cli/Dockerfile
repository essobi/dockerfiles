ARG NODE_VERSION=10.3.0  
FROM node:$NODE_VERSION  
  
LABEL vendor="Infinity Refactoring" \  
git.repository="https://github.com/InfinityRefactoring/docker-angular-cli" \  
authors="Thomás Sousa Silva (ThomasSousa96)"  
  
ARG ANGULAR_CLI_VERSION=6.0.7  
RUN npm install -g @angular/cli@$ANGULAR_CLI_VERSION  
  
WORKDIR /home/node/app/  
  
ENTRYPOINT [ "bash" ]  

