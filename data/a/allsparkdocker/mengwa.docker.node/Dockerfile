FROM node:8.3.0  
MAINTAINER "Neil" neil.zeng@hotmail.com  
ENV HOME=/home/node  
WORKDIR $HOME/app  
COPY ["package.json", "bower.json", "$HOME/app/"]  
RUN useradd --user-group --create-home --shell /bin/false mengwa && \  
mkdir -p $HOME/app && \  
mkdir $HOME/.npm-packages && \  
touch $HOME/.npmrc && \  
echo "prefix=${HOME}/.npm-packages" >> $HOME/.npmrc && \  
echo "cache=${HOME}/.npm/.cache/cnpm" >> $HOME/.npmrc && \  
chown node:node -R $HOME  
USER node  
RUN npm install --global node-sass@4.7.2 && npm install && npm run bower &&
npm run bower-clean  
VOLUME $HOME/app/node_modules  
VOLUME $HOME/app/bower_components  
CMD ["/bin/bash"]  

