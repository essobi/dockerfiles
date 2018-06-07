FROM node:6.9.1  
WORKDIR /app  
COPY package.json /app/package.json  
COPY yarn.lock /app/yarn.lock  
RUN npm install -g yarn  
RUN yarn install  
  
COPY src /app/src  
COPY .git /app/.git  
COPY config /app/config  
COPY gulpfile.babel.js /app/gulpfile.babel.js  
COPY .babelrc /app/.babelrc  
COPY .eslintrc /app/.eslintrc  
COPY .eslintignore /app/.eslintignore  
COPY README.md /app/README.MD  
  
RUN /app/node_modules/gulp/bin/gulp.js build  
CMD ["node", "app/index.js"]  

