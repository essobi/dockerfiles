FROM node:7.5  
RUN npm install -g --save-dev \  
babel-cli \  
babel-preset-es2015 \  
babel-preset-react \  
babel-preset-latest \  
babel-preset-env \  
&& mkdir /app  
  
VOLUME ['/app']  
  
WORKDIR /app  
  
CMD ['babel']  

