FROM xpfriend/workspace-base:3.29.0  
MAINTAINER ototadana@gmail.com  
  
ENV NVM_VERSION v0.33.2  
ENV NODEJS_VERSION v4.8.4  
ENV BOWER_VERSION 1.8.0  
ENV BOWER_NEXUS3_RESOLVER_VERSION 1.0.1  
ENV GRUNT_VERSION 1.2.0  
ENV GULP_VERSION 3.9.1  
ENV NPM_CLI_LOGIN_VERSION 0.0.10  
ENV YO_VERSION 2.0.0  
ENV YARN_VERSION 0.27.5  
RUN sudo wget -qO-
https://raw.githubusercontent.com/creationix/nvm/${NVM_VERSION}/install.sh |
bash  
  
RUN source ~/.nvm/nvm.sh \  
&& nvm install ${NODEJS_VERSION} \  
&& nvm alias default ${NODEJS_VERSION} \  
&& npm install -g bower@${BOWER_VERSION} bower-
nexus3-resolver@${BOWER_NEXUS3_RESOLVER_VERSION} \  
grunt-cli@${GRUNT_VERSION} gulp@${GULP_VERSION} \  
npm-cli-login@${NPM_CLI_LOGIN_VERSION} yo@${YO_VERSION} yarn@${YARN_VERSION}  
RUN sudo ln -s ~/.nvm/nvm.sh /etc/profile.d/nvm.sh  
  
COPY ./config/. /config/  
RUN sudo chown -R owner:owner /config  
RUN chmod +x /config/*  

