FROM node:7.9.0  
WORKDIR /app  
COPY ./webpack.config.js /app/webpack.config.js  
  
RUN npm init -y  
RUN npm install -g webpack  
RUN npm install --save react react-dom  
RUN npm install --save-dev babel-loader babel-core babel-preset-es2015 babel-
preset-react  
  
CMD ["webpack", "-d", "--watch"]  

