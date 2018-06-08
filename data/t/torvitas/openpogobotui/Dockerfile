FROM node:6  
ENV OpenPoGoBotUiVersion 60c422b5bbc8a30242a00df1d6a1d534c58731cc  
ENV OpenPoGoBotUiRepository https://github.com/OpenPoGo/OpenPoGoUI.git  
RUN npm config set progress false -g  
RUN mkdir -p /usr/local/pogobotui && \  
cd /usr/local/pogobotui && \  
git clone ${OpenPoGoBotUiRepository} . && \  
git checkout ${OpenPoGoBotUiVersion} && \  
npm install && \  
node_modules/gulp/bin/gulp.js  
COPY src/ /usr/local/  
WORKDIR /usr/local/pogobotui  
EXPOSE "8080"  
ENTRYPOINT ["bash", "/usr/local/bin/docker-entrypoint.sh"]  
CMD ["npm", "start"]  

