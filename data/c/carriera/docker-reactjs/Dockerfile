FROM node:8-alpine  
  
# webpack and webpack dev middleware  
RUN npm install --save-dev webpack-dev-server  
RUN npm install --save-dev express webpack-dev-middleware  
  
# Dependency for CoreUI-React  
RUN npm install -g eslint-config-react-app@0.3.0 eslint@3.8.1 babel-
eslint@7.0.0 eslint-plugin-react@6.4.1 eslint-plugin-import@2.0.1 eslint-
plugin-jsx-a11y@2.2.3 eslint-plugin-flowtype@2.21.0  
  
# CoreUI for React.js  
RUN npm install coreui.io-react@1.0.0-alpha.6  
  
EXPOSE 3000  
CMD ["npm", "run", "docker-server"]  
  
WORKDIR /app  

