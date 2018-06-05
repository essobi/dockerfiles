FROM node  
MAINTAINER Will Hall <will@willhallonline.co.uk>  
  
# Install required NPM packages globally  
RUN npm install -g eslint eslint-config-airbnb eslint-plugin-react eslint-
plugin-import  
  
# Copy required files and set as executable  
COPY ./eslint.sh /root/eslint.sh  
COPY ./.eslintrc.yml /root/.eslintrc.yml  
RUN chmod +x /root/eslint.sh  
  
WORKDIR /app  
  
# Set entrypoint for sing existing .eslintrc.* or using a default  
ENTRYPOINT ["/root/eslint.sh"]  

