FROM node:latest  
RUN mkdir -p /usr/src  
WORKDIR /usr/src  
RUN npm install -g dockerfile_lint eslint \  
eslint-config-airbnb-base eslint-config-prettier \  
eslint-plugin-import eslint-plugin-prettier \  
htmllint htmllint-cli markdownlint markdownlint-cli \  
prettier stylelint stylelint-config-standard  
COPY . /usr/src  

