FROM node:4  
MAINTAINER elliot.mitchum@ellioseven.com.au  
  
ENV APP_DIR /srv  
ENV APP_NPM_GLOBAL_DIR /home/node/.npm-packages  
# Install global packages to '$APP_NPM_GLOBAL_DIR'.  
RUN mkdir -p $APP_NPM_GLOBAL_DIR \  
&& echo "prefix=$APP_NPM_GLOBAL_DIR" >> /home/node/.npmrc \  
&& echo 'export PATH=$HOME/.npm-packages/bin:$PATH' >> /home/node/.bashrc \  
&& chown -R node:node /home/node  
# Create and configure app directory.  
RUN mkdir -p $APP_DIR \  
&& chown -R node:node $APP_DIR \  
&& echo 'export PATH=$APP_DIR/node_modules/.bin:$PATH' >> /home/node/.bashrc  
  
VOLUME $APP_NPM_GLOBAL_DIR  
WORKDIR $APP_DIR  
USER node  
# Causes container to persist.  
CMD ["tail", "-f", "/dev/null"]  

