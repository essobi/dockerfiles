FROM node:6-alpine  
  
ARG NG_CLI_VERSION  
  
ENV NG_CLI_VERSION ${NG_CLI_VERSION:-1.0.3}  
  
RUN \  
echo "$NG_CLI_VERSION" && \  
npm install -g @angular/cli@${NG_CLI_VERSION} && \  
ng version

