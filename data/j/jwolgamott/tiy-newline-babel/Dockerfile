FROM node  
  
WORKDIR /tmp  
RUN npm install --save-dev babel-cli babel-preset-es2015  
  
RUN echo '{ "presets": ["es2015"] }' > .babelrc  
RUN touch /tmp/code  
CMD ./node_modules/.bin/babel /tmp/code  

