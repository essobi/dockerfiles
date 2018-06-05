FROM node:8  
EXPOSE 8989  
RUN mkdir -p /usr/src/apps/cssgen  
WORKDIR /usr/src/apps/cssgen  
COPY package.json /usr/src/apps/cssgen  
RUN npm install  
RUN npm install forever -g  
RUN npm install gulp -g  
WORKDIR /usr/src/apps/cssgen/trans  
RUN npm install gulp  
WORKDIR /usr/src/apps/cssgen  
RUN npm install --save-dev gulp-uglify  
RUN npm install --save-dev gulp-replace  
RUN npm install --save-dev gulp-sass  
RUN npm install --save-dev gulp-filter  
RUN npm install --save-dev gulp-sassvg  
RUN npm install --save-dev gulp-requirejs  
RUN npm install --save yargs

